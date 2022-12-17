import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;
import java.util.stream.Collectors;

public class Grammar {
    private HashSet<String> nonTerminals;
    private HashSet<String> terminals;
    private HashMap<String, List<String>> productions;
    private String startingSymbol;
    private final String fileName;
    private HashSet<List<String>> canonicalSet;

    public Grammar(String fileName) {
        this.fileName = fileName;
        this.nonTerminals = new HashSet<>();
        this.terminals = new HashSet<>();
        this.productions = new HashMap<>();
        this.canonicalSet = new HashSet<>();
        this.startingSymbol = "";
        readGrammar();
    }

    public void enrichGrammar() {
        productions.put("SR", List.of(String.format(".%S",startingSymbol)));
        nonTerminals.add("SR");
        startingSymbol = "SR";
        buildCanonicalSet();
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
        charArray[indexDot] = charArray[indexDot + 1];
        charArray[indexDot + 1] = '.';
        return String.valueOf(charArray);
    }

    private boolean isDotInFrontOfNonTerminal(String production, String nonTerminal) {
        String rhsProduction = production.split("->")[1].strip();
        int indexDot = rhsProduction.indexOf('.');
        return indexDot != rhsProduction.length() - 1 && rhsProduction.substring(indexDot + 1, indexDot + 2).equals(nonTerminal);
    }

    private String stringRightOfDot(String rhsProduction) {
        int indexDot = rhsProduction.indexOf(".");
        return rhsProduction.substring(indexDot + 1);

    }

    public List<String> closure(List<String> productions) {
        return productions.stream().map(this::closureProduction).flatMap(List::stream).collect(Collectors.toList());
    }

    private List<String> closureProduction(String production) {
        // No dot at the end
        List<String> result = new ArrayList<>();
        result.add(production);
        String next = stringRightOfDot(production).isEmpty()? "" : stringRightOfDot(production).substring(0, 1);
        if (nonTerminals.contains(next)) {
            List<String> productions = this.productions.get(next);
            productions.stream().map(str -> String.format("%s->.%s", next, str)).forEach(res -> {
                if (!result.contains(res)) {
                    result.add(res);
                }
            });
        }
        return result;
    }

    public List<String> goTo(List<String> state, String nonTerminal) {
        return state.stream()
                .filter(prd -> isDotInFrontOfNonTerminal(prd, nonTerminal))
                .map(prd -> closureProduction(moveDotRight(prd)))
                .flatMap(List::stream)
                .collect(Collectors.toList());

    }



    // TODO Documentatie cu link de git, ce tip de parser avem si pe scurt cam cum am implementat noi asta

    private void readGrammar() {
        File grammarFile = new File(fileName);
        try {
            Scanner scanner = new Scanner(grammarFile);
            Arrays.stream(scanner.nextLine().split(" ")).forEach(nt -> this.nonTerminals.add(nt.strip()));
            Arrays.stream(scanner.nextLine().split(" ")).forEach(t -> this.terminals.add(t.strip()));
            this.startingSymbol = scanner.nextLine().strip();
            while (scanner.hasNextLine()) {
                String productionLine = scanner.nextLine().strip();
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
}
