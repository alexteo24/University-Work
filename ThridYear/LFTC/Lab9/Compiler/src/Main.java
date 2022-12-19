import Automaton.FiniteAutomaton;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        List<String> tokens = getTokensList("./token.in");
        List<String> program = readProgram("./p1.txt");
        ProgramScanner scanner = new ProgramScanner(program, tokens);
        try {
            scanner.scan();
        } catch (Exception e) {
            e.printStackTrace();
            System.out.println(e.getMessage());
            return;
        }
//        scanner.saveScannerData();
//        Grammar grammar = new Grammar("./g3.txt");
//        grammar.enrichGrammar();
//        grammar.displayStartingSymbol();
//        grammar.displayNonTerminals();
//        grammar.displayTerminals();
//        grammar.displayProductions();
////        System.out.println(grammar.goTo(grammar.closure(List.of("SR->.A")), "c"));
////        System.out.println(grammar.closure(List.of("SR->.A")));
//        grammar.displayCanonicalSet();
//        System.out.println("grammar.productionsInListForm() = " + grammar.productionsInListForm());
//        try {
//            Parser parser = new Parser(grammar, "a b b c");
//        } catch (Exception e) {
//            e.printStackTrace();
//        }
        String pif = readPif("PIF.OUT");
        Grammar g2Grammar = new Grammar("./g2.txt");
        g2Grammar.enrichGrammar();
        g2Grammar.displayStartingSymbol();
        g2Grammar.displayNonTerminals();
        g2Grammar.displayTerminals();
        g2Grammar.displayProductions();
        g2Grammar.displayCanonicalSet();
        try {
            Parser g2Parser = new Parser(g2Grammar, pif);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }



    public static void processMenu(FiniteAutomaton fa) {
        System.out.println("1. Print states");
        System.out.println("2. Print alphabet");
        System.out.println("3. Print final states");
        System.out.println("4. Print in state");
        System.out.println("5. Print transitions");
        System.out.println("6. Check word with varying length letters");
        System.out.println("0. Exit");
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("Command: ");
            if (scanner.hasNext()) {
                var option = scanner.nextInt();
                switch (option) {
                    case 1 -> fa.printStates();
                    case 2 -> fa.printAlphabet();
                    case 3 -> fa.printFinalStates();
                    case 4 -> fa.printInitialStates();
                    case 5 -> fa.printTransitions();
                    case 6 -> {
                        String sequence = "aaab";
                        var acceptedWord = fa.checkAccepted(sequence);
                        if (!acceptedWord) {
                            System.out.println("Not matching");
                        } else {
                            System.out.println("Matching");
                        }
                    }
                    case 0 -> {
                        return;
                    }
                }
            }

        }
    }

    private static List<String> getTokensList(String inputFile) {
        List<String> tokens = new ArrayList<>();
        tokens.add("ID");
        tokens.add("INT_CONST");
        tokens.add("STR_CONST");
        try {
            File tokenFile = new File(inputFile);
            Scanner scannerFile = new Scanner(tokenFile);
            while (scannerFile.hasNextLine()) {
                String token = scannerFile.nextLine();
                tokens.add(token);
            }
            scannerFile.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        return tokens;
    }

    private static List<String> readProgram(String inputFile) {
        List<String> program = new ArrayList<>();
        try {
            File programFile = new File(inputFile);
            Scanner scannerFile = new Scanner(programFile);
            while (scannerFile.hasNextLine()) {
                String programLine = scannerFile.nextLine();
                program.add(programLine.strip());
            }
            scannerFile.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        return program;
    }

    private static String readPif(String inputFile) {
        StringBuilder result = new StringBuilder();
        try {
            File programFile = new File(inputFile);
            Scanner scannerFile = new Scanner(programFile);
            while (scannerFile.hasNextLine()) {
                String programLine = scannerFile.nextLine();
                result.append(programLine.split("<->")[0].strip()).append(" ");
            }
            result.replace(result.length() -1, result.length() - 1, "");
            scannerFile.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        return result.toString();
    }
}
