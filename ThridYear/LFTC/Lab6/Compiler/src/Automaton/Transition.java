package Automaton;

public class Transition {
    private final String currentState;
    private final String nextState;
    private final String label;

    public Transition(String currentState, String nextState, String label) {
        this.currentState = currentState;
        this.nextState = nextState;
        this.label = label;
    }

    public String getCurrentState() {
        return currentState;
    }

    public String getNextState() {
        return nextState;
    }

    public String getLabel() {
        return label;
    }

    @Override
    public String toString() {
        return "Transition{" +
                 currentState + "," +
                nextState + "," +
                label +
                '}';
    }
}
