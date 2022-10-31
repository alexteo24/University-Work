import BinarySearchTree.BST;
import Pair.Pair;

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
        scanner.saveScannerData();
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
