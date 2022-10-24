import BinarySearchTree.BST;
import Pair.Pair;

import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class ProgramScanner {
    private BST<Pair<String, Integer>> symbolTable;
    private List<String> program;
    private List<String> tokens;
    private Integer currentLine;
    private Integer index;

    public ProgramScanner(List<String> program, List<String> tokens) {
        this.symbolTable = new BST<Pair<String, Integer>>();
        this.program = program;
        this.tokens = tokens;
        this.index = 0;
        this.currentLine = 0;
    }

    private boolean parseIdentifier() {
        Pattern pattern = Pattern.compile("^([a-zA-z]+[0-9]*)");
        Matcher matcher = pattern.matcher(program.get(currentLine).substring(index));
        boolean result = matcher.find();
        if (!result) {
            return false;
        }
        String identifier = matcher.group(1);
        index += identifier.length();
        symbolTable.add(new Pair<>(identifier, 1));
        return true;
    }

    private boolean parseString() {
        Pattern pattern = Pattern.compile("^(\"[a-zA-Z0-9]*\")");
        Matcher matcher = pattern.matcher(program.get(currentLine).substring(index));
        boolean result = matcher.find();
        if (!result) {
            return false;
        }
        String stringConstant = matcher.group(1);
        stringConstant = stringConstant.substring(1, stringConstant.length() - 2);
        index += stringConstant.length();
        symbolTable.add(new Pair<>(stringConstant, 1));
        return true;
    }

    private boolean parseInt() {
        Pattern pattern = Pattern.compile("^(0|[1-9]+[0-9]*)");
        Matcher matcher = pattern.matcher(program.get(currentLine).substring(index));
        boolean result = matcher.find();
        if (!result) {
            return false;
        }
        String intConstant = matcher.group(1);
        index += intConstant.length();
        symbolTable.add(new Pair<>(intConstant, 1)); //TODO: replace 1 with something meaningful in the next labs
        return true;
    }

    private boolean parseTokens() {
        for(int i = 0; i < tokens.size(); i++) {
            if (program.get(currentLine).substring(index).startsWith(tokens.get(i))) {
                index += tokens.get(i).length();
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
                index++;
            }
        }
    }

    private void next() throws Exception {
        skipWhitespace();
        if (parseIdentifier() || parseInt() || parseString() || parseTokens()) {
            if (index == program.get(currentLine).length()) {
                index = 0;
                currentLine++;
            }
            return;
        }
        throw new Exception("Lexical error: Cannot classify token on line " + currentLine.toString());
    }

    public void scan() throws Exception {
        while (currentLine <= program.size() - 1) {
            next();
        }
    }

    public void displayST() {
        symbolTable.displayTree();
    }




}
