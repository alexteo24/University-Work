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

    public Grammar(String fileName) {
        this.fileName = fileName;
        this.nonTerminals = new HashSet<>();
        this.terminals = new HashSet<>();
        this.productions = new HashMap<>();
        this.startingSymbol = "";
        readGrammar();
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
                String key = productionLine.split("->")[0].strip();
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
    public boolean checkIfCFG() {
        return false;
    }
}
