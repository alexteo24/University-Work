package Automaton;

import java.io.File;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

public class FiniteAutomaton {
    private List<String> states;
    private String initialState;
    private List<String> finalStates;
    private List<String> alphabet;
    private List<Transition> transitions;

    private String filePath;

    public FiniteAutomaton(String fileName) {
        this.filePath = fileName;
        readFiniteAutomaton();
    }

    private void readFiniteAutomaton() {
        File finiteAutomatonFile = new File(filePath);
        try {
            Scanner myScanner = new Scanner(finiteAutomatonFile);
            while (myScanner.hasNextLine()) {
                String[] currentLine = myScanner.nextLine().split("=");
                switch (currentLine[0].strip()) {
                    case "states" -> states = Arrays.stream(currentLine[1].substring(1, currentLine[1].length() - 1).split(", *"))
                            .filter(string -> !string.isEmpty())
                            .map(String::strip)
                            .collect(Collectors.toList());
                    case "in_state" -> initialState = currentLine[1].strip();
                    case "out_states" -> finalStates = Arrays.stream(currentLine[1].substring(1, currentLine[1].length() - 1).split(", *"))
                            .filter(string -> !string.isEmpty())
                            .map(String::strip)
                            .collect(Collectors.toList());
                    case "alphabet" -> alphabet = Arrays.stream(currentLine[1].substring(1, currentLine[1].length() - 1).split(", *"))
                            .filter(string -> !string.isEmpty())
                            .map(String::strip)
                            .collect(Collectors.toList());
                    case "transitions" -> transitions = Arrays.stream(currentLine[1].substring(1, currentLine[1].length() - 1).split("; *"))
                            .filter(string -> !string.isEmpty())
                            .map(string -> {
                                var transition = string.strip().substring(1, string.length() - 1).split(", *");
                                return new Transition(transition[0], transition[1], transition[2]);
                            })
                            .collect(Collectors.toList());
                    default -> throw new Exception("Invalid line in FA!");
                }
            }
            myScanner.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public boolean checkAccepted(String word) {
        var state = initialState;
        for (int i = 0; i < word.length(); i++) {
            var letter = word.substring(i, i + 1);
            String newState = "";
            for (var transition: transitions) {
                if (transition.getCurrentState().equals(state) && transition.getLabel().equals(letter)) {
                    newState = transition.getNextState();
                    break;
                }
            }
            if (newState.isEmpty()) {
                return false;
            }
            state = newState;
        }
        return this.finalStates.contains(state);
    }

    public String getNextAccepted(String word) {
        var state = initialState;
        StringBuilder acceptedWord = new StringBuilder();
        for (int i = 0; i < word.length(); i++) {
            var letter = word.substring(i, i + 1);
            if(letter.equals(" ")) {
                break;
            }
            String newState = "";
            for (var transition : transitions) {
                if (transition.getCurrentState().equals(state) && transition.getLabel().equals(letter)) {
                    newState = transition.getNextState();
                    break;
                }
            }
            if (newState.isEmpty()) {
                break;
            }
            state = newState;
            acceptedWord.append(letter);
        }
        if(!this.finalStates.contains(state)) {
            return "";
        }
        return acceptedWord.toString();
    }

    public void printStates() {
        System.out.println("states = " + states);
    }
    public void printInitialStates() {
        System.out.println("initialState = " + initialState);
    }
    public void printFinalStates() {
        System.out.println("finalStates = " + finalStates);
    }
    public void printAlphabet() {
        System.out.println("alphabet = " + alphabet);
    }
    public void printTransitions() {
        System.out.println("transitions = " + transitions);
    }

    public void printEverything() {
        System.out.println("states = " + states);
        System.out.println("initialState = " + initialState);
        System.out.println("finalStates = " + finalStates);
        System.out.println("alphabet = " + alphabet);
        System.out.println("transitions = " + transitions);
    }
}
