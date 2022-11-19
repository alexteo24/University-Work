import Automaton.FiniteAutomaton;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        List<String> tokens = getTokensList("./token.in");
        List<String> program = readProgram("./p3.txt");
        ProgramScanner scanner = new ProgramScanner(program, tokens);
        try {
            scanner.scan();
        } catch (Exception e) {
            e.printStackTrace();
            System.out.println(e.getMessage());
            return;
        }
        FiniteAutomaton fa = new FiniteAutomaton("./test_fa.in");
        processMenu(fa);
        scanner.saveScannerData();
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
        tokens.add("CONST");
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
}
