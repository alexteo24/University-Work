import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;
import java.util.stream.Collectors;

public class Grammar {
    private final HashSet<String> nonTerminals;
    private final HashSet<String> terminals;
    private final HashMap<String, List<String>> productions;
    private final List<String> productionsList;
    private String startingSymbol;
    private final String fileName;
    private String previousStartingSymbol;
    private final List<List<String>> canonicalSet;

    public Grammar(String fileName) {
        this.fileName = fileName;
        this.nonTerminals = new HashSet<>();
        this.terminals = new HashSet<>();
        this.productions = new HashMap<>();
        this.productionsList = new ArrayList<>();
        this.canonicalSet = new ArrayList<>();
        this.startingSymbol = "";
        this.previousStartingSymbol = "";
        readGrammar();
    }

    public void enrichGrammar() {
        productions.put("SR", List.of(String.format(".%s",startingSymbol)));
        nonTerminals.add("SR");
        previousStartingSymbol = startingSymbol;
        startingSymbol = "SR";
        buildCanonicalSet();
    }

    public List<String> productionsInListForm() {
//        List<String> result = new ArrayList<>();
//        productions.forEach((k, v) -> {
//            v.forEach(pr -> {
//                result.add(String.format("%s->%s", k, pr));
//            });
//        });
        return productionsList;
    }

    private void buildCanonicalSet() {
        Queue<List<String>> queue = new ArrayDeque<>();
        List<String> initialState = closureProduction(getInitialProductionAfterEnrich());
        canonicalSet.add(initialState);
        queue.add(initialState);
        while (!queue.isEmpty()) {
            List<String> nextState = queue.poll();
            nonTerminals.forEach(nt -> {
                var list = goTo(nextState, nt);
                if(!canonicalSet.contains(list) && !list.isEmpty()) {
                    queue.add(list);
                    canonicalSet.add(list);
                }
            });
            terminals.forEach(nt -> {
                var list = goTo(nextState, nt);
                if(!canonicalSet.contains(list) && !list.isEmpty()) {
                    queue.add(list);
                    canonicalSet.add(list);
                }
            });
        }

    }


    private String getInitialProductionAfterEnrich() {
        String production = String.join("", productions.get(startingSymbol));
        return String.format("%s->%s", startingSymbol, production);
    }

    private String moveDotRight(String rhsProduction) {
        int indexDot = rhsProduction.indexOf(".");
        //.AB -> AB -> A.B
        var charArray = rhsProduction.toCharArray();
        int spaceIndex = rhsProduction.indexOf(" ", indexDot);
        var result = new StringBuilder();
        result.append(rhsProduction, 0, indexDot);
        if (spaceIndex == -1) {
            result.append(rhsProduction.substring(indexDot + 1));
            result.append(".");
        } else {
            result.append(rhsProduction, indexDot + 1, spaceIndex + 1);
            result.append(".");
            result.append(rhsProduction.substring(spaceIndex + 1));
        }
        return result.toString();
    }

    private boolean isDotInFrontOfNonTerminal(String production, String nonTerminal) {
        String rhsProduction = production.split("->")[1].strip();
        int indexDot = rhsProduction.indexOf('.');
        int spaceIndex = rhsProduction.indexOf(" ", indexDot);
        if (spaceIndex != -1) {
            return indexDot != rhsProduction.length() - 1 && rhsProduction.substring(indexDot + 1, spaceIndex).equals(nonTerminal);
        }
        return indexDot != rhsProduction.length() - 1 && rhsProduction.substring(indexDot + 1).equals(nonTerminal);

    }

    public static String stringRightOfDot(String rhsProduction) {
        int indexDot = rhsProduction.indexOf(".");
        int indexSpace = rhsProduction.indexOf(" ", indexDot);
        if (indexSpace != -1) {
            return rhsProduction.substring(indexDot + 1, indexSpace);
        }
        return rhsProduction.substring(indexDot + 1);

    }

    public List<String> closure(List<String> productions) {
        List<String> result = new ArrayList<>();
        productions.stream().map(this::closureProduction).flatMap(List::stream).forEach(pr -> {
            if (!result.contains(pr)) {
                result.add(pr);
            }
        });
        return result;
    }

    private List<String> closureProduction(String production) {
        // No dot at the end
        List<String> result = new ArrayList<>();
        result.add(production);
        Queue<String> queue = new ArrayDeque<>();
        queue.add(production);
        while (!queue.isEmpty()) {
            String current = queue.poll();
            String next = stringRightOfDot(current);
            if (next.isEmpty()) {
                continue;
            }
            if (nonTerminals.contains(next)) {
                List<String> productions = this.productions.get(next);
                productions.stream().map(str -> String.format("%s -> .%s", next, str)).forEach(res -> {
                    if (!result.contains(res)) {
                        result.add(res);
                        queue.add(res);
                    }
                });
            }
        }
        return result;
    }

    public List<String> goTo(List<String> state, String token) {
        var filtered = state.stream()
                .filter(prd -> isDotInFrontOfNonTerminal(prd, token))
                .map(this::moveDotRight)
                .collect(Collectors.toList());
        return closure(filtered);

    }

    private void readGrammar() {
        File grammarFile = new File(fileName);
        try {
            Scanner scanner = new Scanner(grammarFile);
            Arrays.stream(scanner.nextLine().split(" ")).forEach(nt -> this.nonTerminals.add(nt.strip()));
            Arrays.stream(scanner.nextLine().split(" ")).forEach(t -> this.terminals.add(t.strip()));
            this.startingSymbol = scanner.nextLine().strip();
            while (scanner.hasNextLine()) {
                String productionLine = scanner.nextLine().strip();
                productionsList.add(productionLine);
                String key = productionLine.split("->")[0].strip();
                nonTerminals.add(key);
                List<String> oldProductions = this.productions.containsKey(key)
                        ? this.productions.get(key)
                        : new ArrayList<>();
                String[] productionsList = productionLine.split("->")[1].split("\\|");
                Arrays.stream(productionsList).forEach(pr -> {
                    oldProductions.add(pr.strip());
                });
                this.productions.put(key, oldProductions);
            }
            scanner.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }

    public void displayNonTerminals() {
        StringBuilder stringBuilder = new StringBuilder();
        this.nonTerminals.forEach(nt -> stringBuilder.append(nt).append(" "));
        System.out.println(stringBuilder);
    }

    public void displayTerminals() {
        StringBuilder stringBuilder = new StringBuilder();
        this.terminals.forEach(t -> stringBuilder.append(t).append(" "));
        System.out.println(stringBuilder);
    }

    public void displayProductions() {
        StringBuilder stringBuilder = new StringBuilder();
        this.productions.forEach((k, v) -> {
            stringBuilder.append(k).append(" -> ");
            v.forEach(production -> stringBuilder.append(production).append(" | "));
            stringBuilder.deleteCharAt(stringBuilder.lastIndexOf("|"));
            stringBuilder.append("\n");
        });
        System.out.println(stringBuilder);
    }

    public void displayProductionsForNonTerminal(String nonTerminal) {
        if (this.productions.containsKey(nonTerminal)) {
            StringBuilder stringBuilder = new StringBuilder();
            stringBuilder.append(nonTerminal).append(" -> ");
            this.productions.get(nonTerminal).forEach(production -> stringBuilder.append(production).append(" | "));
            stringBuilder.deleteCharAt(stringBuilder.lastIndexOf("|"));
            System.out.println(stringBuilder);
        } else {
                System.out.println("");
        }
    }

    public void displayStartingSymbol() {
        System.out.println(startingSymbol);
    }

    public void displayCanonicalSet() {
        System.out.println(canonicalSet);
    }

    public boolean checkIfCFG() {
        for (String nonTerminal : nonTerminals) {
            for(int i = 0; i < nonTerminal.length(); i++) {
                if (terminals.contains(nonTerminal.substring(i, i + 1))) {
                    return false;
                }
            }
        }
        return true;
    }

    public List<List<String>> getCanonicalSet() {
        return canonicalSet;
    }

    public HashSet<String> getNonTerminals() {
        return nonTerminals;
    }

    public HashSet<String> getTerminals() {
        return terminals;
    }

    public String getPreviousStartingSymbol() {
        return previousStartingSymbol;
    }

    public HashMap<String, List<String>> getProductions() {
        return productions;
    }
}
