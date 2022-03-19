package Model;

import Exceptions.MyException;
import Model.ADT.*;
import Model.Statements.IStatement;
import Model.Values.Value;

import java.io.BufferedReader;
import java.util.Map;
import java.util.Random;
import Model.ADT.MyILatchTable;

public class ProgramState {
    private final MyIStack<IStatement> executionStack;
    private final MyIDictionary<String, Value> symTable;
    private final MyIList<String> out;
    private final MyIDictionary<String, BufferedReader> fileTable;
    private final MyIHeap heap;
    private final MyILatchTable latchTable;
    private int id;
    private static int lastID = 0;

    public ProgramState(IStatement originalProgram) {
        executionStack = new MyStack<>();
        symTable = new MyDict<>();
        out = new MyList<>();
        executionStack.push(originalProgram);
        heap = new MyHeap();
        fileTable = new MyDict<>();
        latchTable = new MyLatchTable();
        id = setId();
    }

    public ProgramState(MyIStack<IStatement> executionStack,
                        MyIDictionary<String, Value> symTable,
                        MyIList<String> out,
                        MyIDictionary<String, BufferedReader> fileTable,
                        MyIHeap heap,
                        MyILatchTable latchTable) {
        this.executionStack = executionStack;
        this.symTable = symTable;
        this.out = out;
        this.heap = heap;
        this.fileTable = fileTable;
        this.latchTable = latchTable;
        id = setId();
    }

    public MyIHeap getHeap() {
        return heap;
    }

    public MyILatchTable getLatchTable() { return latchTable; }

    private synchronized int setId() {
        lastID++;
        return lastID;
    }

    public MyIStack<IStatement> getExecutionStack() {
        return executionStack;
    }

    public MyIDictionary<String, Value> getSymTable() {
        return symTable;
    }

    public MyIList<String> getOut() {
        return out;
    }

    public MyIDictionary<String, BufferedReader> getFileTable() {
        return fileTable;
    }

    public Integer getId() { return id; }

    public String executionStackToString() {
        StringBuilder stringBuilder = new StringBuilder();
        for (IStatement statement : executionStack) {
            stringBuilder.append("[\n").append(statement.toString()).append("\n]\n");
        }
        return stringBuilder.toString();
    }

    public String symbolTableToString() throws MyException {
        StringBuilder stringBuilder = new StringBuilder();
        for (String key : symTable.keySet()) {
            stringBuilder.append(String.format("%s:%s\n", key, symTable.getValue(key).toString()));
        }
        return stringBuilder.toString();
    }

    public String outToString() {
        StringBuilder stringBuilder = new StringBuilder();
        for (String item : out) {
            stringBuilder.append(item).append("\n");
        }
        return stringBuilder.toString();
    }

    public String fileTableToString() {
        StringBuilder stringBuilder = new StringBuilder();
        for (String key : fileTable.keySet()) {
            stringBuilder.append(key).append("\n");
        }
        return stringBuilder.toString();
    }

    public ProgramState oneStep() throws MyException {
        if (executionStack.isEmpty())
            throw new MyException("Program state stack is empty.");
        IStatement currentStatement = executionStack.pop();
        return currentStatement.execute(this);
    }

    public String heapToString() {
        StringBuilder outStringBuilder = new StringBuilder();
        Map<Integer, Value> map = heap.getContent();
        for (Integer key : map.keySet())
            outStringBuilder.append(key).append(" -> ").append(map.get(key)).append("\n");
        return outStringBuilder.toString();
    }

    public String latchTableToString() throws MyException {
        StringBuilder latchTableStringBuilder = new StringBuilder();
        for (int key : latchTable.getLatchTable().keySet()) {
            latchTableStringBuilder.append(String.format("%d -> %d\n", key, latchTable.get(key)));
        }
        return latchTableStringBuilder.toString();
    }

    public boolean isNotCompleted() {
        return !executionStack.isEmpty();
    }

    @Override
    public String toString() {
        try {
            return "ID: " + id + "\nExecution stack: " + executionStackToString() + "\nSymbol table: " + symbolTableToString() + "\nOutput list: " + outToString()
                    + "\nFile table: " + fileTableToString() + "\nHeap table: " + heapToString() + "\nLatch table: " + latchTableToString() + "\n----------------------------------------------------\n";
        } catch (MyException e) {
            e.printStackTrace();
        }
        return "";
    }

}
