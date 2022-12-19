import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.*;

public class Parser {
    private final Grammar grammar;
    private final List<ParsingTableItem> parsingTable;
    private final Stack<String> workStack;
    private final Queue<String> input;
    private final Stack<Integer> output;
    private final List<ParentSiblingNode> parserTree;

    public Parser(Grammar grammar, String sequenceToParse) throws Exception {
        this.grammar = grammar;
        this.parsingTable = new ArrayList<>();
        this.workStack = new Stack<>();
        this.input = new ArrayDeque<>();
        this.output = new Stack<>();
        this.parserTree = new ArrayList<>();
        prepareForParsing(sequenceToParse);
        buildParsingTable();
        parseTheSequence();
        constructParserTree();
        saveOutputToFile();
    }

    private void constructParserTree() {
        List<String> productions = grammar.productionsInListForm();
        HashSet<String> nonTerminals = grammar.getNonTerminals();
        int nextNonTerminalIndex = 0;
        while (!output.isEmpty()) {
            int productionNumber = output.pop();
            String[] tokens = productions.get(productionNumber).split("->");
            String lhsProduction = tokens[0].strip();
            String rhsProduction = tokens[1].strip();
            if (parserTree.isEmpty()) {
                parserTree.add(new ParentSiblingNode(lhsProduction, -1, -1));
                String[] rhsTokens = rhsProduction.split(" ");
                for (int i = 0; i < rhsTokens.length; i++) {
                    parserTree.add(new ParentSiblingNode(rhsTokens[i], 0, parserTree.size() + 1));
                }
                parserTree.get(parserTree.size() - 1).setRightSibling(-1);
            } else {
                nextNonTerminalIndex++;
                while (!nonTerminals.contains(parserTree.get(nextNonTerminalIndex).getInfo())) {
                    nextNonTerminalIndex++;
                }
                String[] rhsTokens = rhsProduction.split(" ");
                for (int i = 0; i < rhsTokens.length; i++) {
                    parserTree.add(new ParentSiblingNode(rhsTokens[i], nextNonTerminalIndex, parserTree.size() + 1));
                }
                parserTree.get(parserTree.size() - 1).setRightSibling(-1);
            }
        }
    }

    private void prepareForParsing(String sequenceToParse) {
        input.addAll(Arrays.asList(sequenceToParse.split(" ")));
        workStack.push("0");
    }

    private void parseTheSequence() {
        List<String> productions = grammar.productionsInListForm();
        while (true) {
            int topNumber = Integer.parseInt(workStack.peek());
            ParsingTableItem parsingTableItem = parsingTable.get(topNumber);
            String action = parsingTableItem.getAction();
            if (action.contains("shift reduce")) {
                if (!input.isEmpty()) {
                    var item = parsingTableItem.getGoTo().get(input.peek());
                    if (item != null) {
                        String nextInput = input.poll();
                        workStack.push(nextInput);
                        workStack.push(parsingTableItem.getGoTo().get(nextInput).toString());
                        continue;
                    }
                }
            }
            if (action.contains("reduce")) {
                int productionNumber = action.contains(" ")
                    ? Integer.parseInt(action.split(" ")[1].split(",")[1])
                    : Integer.parseInt(action.split(",")[1]);
                String production = productions.get(productionNumber);
                String[] split = production.split("->");
                String rhsProduction = split[0].strip();
                String lhsProduction = split[1].strip();
                var tokens = lhsProduction.split(" ");
                for (int i = tokens.length - 1; i >= 0; i--) {
                    workStack.pop();
                    workStack.pop();
                }

                output.push(productionNumber);
                topNumber = Integer.parseInt(workStack.peek());
                workStack.push(rhsProduction);
                topNumber = parsingTable.get(topNumber).getGoTo().get(rhsProduction);
                workStack.push(String.valueOf(topNumber));
                continue;
            }
            if (action.contains("shift")) {
                String nextInput = input.poll();
                workStack.push(nextInput);
                workStack.push(parsingTableItem.getGoTo().get(nextInput).toString());
                continue;

            }
            if (action.contains("acc")) {
                break;
            }

        }
    }

    private void buildParsingTable() throws Exception {
        List<String> productions = grammar.productionsInListForm();
        List<List<String>> canonicalSet = grammar.getCanonicalSet();
        for (int i = 0; i < canonicalSet.size(); i++) {
            List<String> currentState = canonicalSet.get(i);
            String action = "";
            ParsingTableItem parsingTableItem = new ParsingTableItem("");
            int dotCount = currentState.stream().filter(prod -> prod.endsWith(".")).map(pr -> 1).reduce(0, Integer::sum);
            if (dotCount == 1) {
                if (currentState.size() == 1) {
                    if (currentState.get(0).split("->")[1].equals(String.format("%s.", grammar.getPreviousStartingSymbol()))) {
                        action = "acc";
                    } else {
                        action = String.format("reduce,%d", productions.indexOf(currentState.get(0).replaceAll("\\.", "")));
                    }
                } else {
                    for (int j = 0; j < currentState.size(); j++) {
                        String currentProd = currentState.get(j);
                        String result = Grammar.stringRightOfDot(currentProd);
                        if (result.isEmpty()) {
                            action = String.format("shift reduce,%d", productions.indexOf(currentProd.replaceAll("\\.", "")));
                        } else {
                            grammar.getTerminals().forEach(t -> {
                                var goTo = grammar.goTo(currentState, t);
                                int index = canonicalSet.indexOf(goTo);
                                if (index != -1) {
                                    parsingTableItem.getGoTo().put(t,index);
                                }

                            });
                            grammar.getNonTerminals().forEach(t -> {
                                var goTo = grammar.goTo(currentState, t);
                                int index = canonicalSet.indexOf(goTo);
                                if (index != -1) {
                                    parsingTableItem.getGoTo().put(t,index);
                                }

                            });
                        }
                    }

                }
            } else if (dotCount == 0) {
                action = "shift";
                grammar.getTerminals().forEach(t -> {
                    var goTo = grammar.goTo(currentState, t);
                    int index = canonicalSet.indexOf(goTo);
                    if (index != -1) {
                        parsingTableItem.getGoTo().put(t,index);
                    }

                });
                grammar.getNonTerminals().forEach(t -> {
                    var goTo = grammar.goTo(currentState, t);
                    int index = canonicalSet.indexOf(goTo);
                    if (index != -1) {
                        parsingTableItem.getGoTo().put(t,index);
                    }

                });
            } else {
                throw new Exception("Reduce conflict");
            }
            parsingTableItem.setAction(action);
            parsingTable.add(parsingTableItem);
        }
    }


    private void saveOutputToFile() {
        try {
            File parserTreeFile = new File("output2.txt");
            parserTreeFile.createNewFile();
            FileWriter myWriter = new FileWriter("output2.txt");
            for (ParentSiblingNode parentSiblingNode : parserTree) {
                myWriter.write(parentSiblingNode.toString());
                myWriter.write("\n");
            }
            myWriter.close();
        } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }

    @Override
    public String toString() {
        return "Parser{" +
                "grammar=" + grammar +
                '}';
    }
}

class ParsingTableItem {
    private String action;
    private HashMap<String, Integer> goTo;
    private boolean conflict;

    public ParsingTableItem(String action) {
        this.action = action;
        this.goTo = new HashMap<>();
        this.conflict = false;
    }

    public void addAction(String action) {
        this.action = String.format("%s %s", action, this.action);
    }

    public String getAction() {
        return action;
    }


    public void setAction(String action) {
        this.action = action;
    }

    public HashMap<String, Integer> getGoTo() {
        return goTo;
    }

    public void setGoTo(HashMap<String, Integer> goTo) {
        this.goTo = goTo;
    }

    public boolean isConflict() {
        return conflict;
    }

    public void setConflict(boolean conflict) {
        this.conflict = conflict;
    }

    @Override
    public String toString() {
        return "ParsingTableItem{" +
                "action='" + action + '\'' +
                ", goTo=" + goTo +
                '}';
    }
}
