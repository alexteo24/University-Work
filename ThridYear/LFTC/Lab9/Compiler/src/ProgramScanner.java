import Automaton.FiniteAutomaton;
import BinarySearchTree.BST;
import LinkedList.LinkedList;
import Pair.Pair;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.List;
import java.util.Objects;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class ProgramScanner {
    private BST<Pair<String, Integer>> symbolTable;
    private LinkedList<Pair<String, Integer>> pif;
    private List<String> program;
    private List<String> tokens;
    private Integer currentLine;
    private Integer index;
    private Integer nrBlocks;
    private Integer previousIndex;

    public ProgramScanner(List<String> program, List<String> tokens) {
        this.symbolTable = new BST<>();
        this.program = program;
        this.tokens = tokens;
        this.index = 0;
        this.previousIndex = 0;
        this.currentLine = 0;
        this.pif = new LinkedList<Pair<String, Integer>>();
        this.nrBlocks = 0;
    }

    private boolean parseIdentifier() {
        if (!checkNear()) {
            return false;
        }
//        Pattern pattern = Pattern.compile("^([a-zA-z]+[0-9]*)");
//        Matcher matcher = pattern.matcher(program.get(currentLine).substring(index));
//        boolean result = matcher.find();
//        if (!result) {
//            return false;
//        }
//        String identifier = matcher.group(1).split("[\\[\\]]")[0];
        var fa = new FiniteAutomaton("identifier.in");
        var identifier = fa.getNextAccepted(program.get(currentLine).substring(index));
        if (identifier.isEmpty()) {
            return false;
        }
        previousIndex = index;
        index += identifier.length();
        var element = symbolTable.find(new Pair<>(identifier, 0));
        if (element != null) {
            pif.add(new Pair<>(String.format("ID <-> %d", tokens.indexOf("ID")),element.getValue()));
        } else {
            symbolTable.add(new Pair<>(identifier, symbolTable.getLength()));
            pif.add(new Pair<>(String.format("ID <-> %d", tokens.indexOf("ID")), symbolTable.getLength() - 1));
        }
        return true;
    }

    private boolean parseString() throws Exception {
        if (!checkNear()) {
            return false;
        }
        Pattern pattern = Pattern.compile("^(\"[a-zA-Z0-9]*\")");
        Matcher matcher = pattern.matcher(program.get(currentLine).substring(index));
        boolean result = matcher.find();
        if (!result) {
            pattern = Pattern.compile("^(\"[a-zA-Z0-9]*[^a-zA-Z0-9]+[a-zA-Z0-9]*\")");
            matcher = pattern.matcher(program.get(currentLine).substring(index));
            result = matcher.find();
            if (result) {
                throw new Exception("Lexical error: Invalid characters inside string on line " + currentLine);
            }
            pattern = Pattern.compile("^(\"[a-zA-Z0-9]*)");
            matcher = pattern.matcher(program.get(currentLine).substring(index));
            result = matcher.find();
            if (result) {
                throw new Exception("Lexical error: Unclosed quotes on line " + currentLine);
            }
            return false;
        }
        String stringConstant = matcher.group(1);
        stringConstant = stringConstant.substring(1, stringConstant.length() - 1);
        previousIndex = index;
        index += stringConstant.length()+2;
        var element = symbolTable.find(new Pair<>(stringConstant, 0));
        if (element != null) {
            pif.add(new Pair<>(String.format("STR_CONST <-> %d", tokens.indexOf("STR_CONST")),element.getValue()));
        } else {
            symbolTable.add(new Pair<>(stringConstant, symbolTable.getLength()));
            pif.add(new Pair<>(String.format("STR_CONST <-> %d", tokens.indexOf("STR_CONST")), symbolTable.getLength() - 1));
        }
        return true;
    }

    private boolean parseInt() {
        if (!checkNear()) {
            return false;
        }
//        Pattern pattern = Pattern.compile("^(0|[1-9]+[0-9]*)");
//        Matcher matcher = pattern.matcher(program.get(currentLine).substring(index));
//        boolean result = matcher.find();
//        if (!result) {
//            return false;
//        }
        var fa = new FiniteAutomaton("int_constant.in");
        var intConstant = fa.getNextAccepted(program.get(currentLine).substring(index));
        if (intConstant.isEmpty()) {
            return false;
        }
//        String intConstant = matcher.group(1);
        previousIndex = index;
        index += intConstant.length();
        var element = symbolTable.find(new Pair<>(intConstant, 0));
        if (element != null) {
            pif.add(new Pair<>(String.format("INT_CONST <-> %d", tokens.indexOf("INT_CONST")),element.getValue()));
        } else {
            symbolTable.add(new Pair<>(intConstant, symbolTable.getLength()));
            pif.add(new Pair<>(String.format("INT_CONST <-> %d", tokens.indexOf("INT_CONST")), symbolTable.getLength() - 1));
        }
        return true;
    }

    private boolean parseTokens() {
        for(int i = 0; i < tokens.size(); i++) {
            if (program.get(currentLine).substring(index).startsWith(tokens.get(i))) {
                previousIndex = index;
                index += tokens.get(i).length();
                if(Objects.equals(tokens.get(i), "{")) {
                    nrBlocks++;
                } else if (Objects.equals(tokens.get(i), "}")) {
                    nrBlocks--;
                }
                pif.add(new Pair<>(String.format("%s <-> %d", tokens.get(i), i), -1));
                return true;
            }
        }
        return false;
    }

    private void skipWhitespace() {
        while (currentLine != program.size() && program.get(currentLine).charAt(index) == ' ') {
            if (index == program.get(currentLine).length()) {
                index = 0;
                currentLine++;
            } else {
                previousIndex = index;
                index++;
            }
        }
    }

    private void next() throws Exception {
        skipWhitespace();
        if (parseInt() || parseString() || parseTokens() || parseIdentifier()) {
            if (index == program.get(currentLine).length()) {
                index = 0;
                currentLine++;
            }
            return;
        }
        throw new Exception("Lexical error: Cannot classify token on line " + currentLine.toString() +
                "\n Token: " + getUnclassifiedToken());
    }

    private String getUnclassifiedToken() {
        String regex = "[+=!()\\[\\]\\- ]";
        return program.get(currentLine).substring(previousIndex).split(regex)[0];
    }


    private boolean checkNear() {
        boolean ok = false;
        if (index < 2) {
            return true;
        }
        for (var token: tokens) {
            if (program.get(currentLine).substring(index-2).startsWith(token)) {
                ok = true;
                break;
            }
            if (program.get(currentLine).substring(index-1).startsWith(token) ||
                    program.get(currentLine).charAt(index - 1) == ' ') {
                ok = true;
                break;
            }
        }
        return ok;
    }

    public void scan() throws Exception {
        while (currentLine <= program.size() - 1) {
            next();
        }
        if (nrBlocks != 0) {
            throw new Exception("Invalid opening/closing of blocks! " + currentLine);
        }
    }

    public void saveScannerData() {
        try {
            File st = new File("ST.out");
            st.createNewFile();
            FileWriter myWriter = new FileWriter("ST.out");
            myWriter.write(symbolTable.displayTree());
            myWriter.close();

            File pif = new File("PIF.out");
            pif.createNewFile();
            myWriter = new FileWriter("PIF.out");
            myWriter.write(this.pif.displayList());
            myWriter.close();
        } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }

    public void display() {
        System.out.println("Symbol table:");
        symbolTable.displayTree();
        System.out.println("\n\n\nPIF:");
        pif.displayList();
    }
}
