package View.GUI;

import Controller.Controller;
import Exceptions.MyException;
import Model.ADT.MyDict;
import Model.ADT.MyHeap;
import Model.ADT.MyList;
import Model.ADT.MyStack;
import Model.Expressions.*;
import Model.ProgramState;
import Model.Statements.*;
import Model.Types.BoolType;
import Model.Types.IntType;
import Model.Types.ReferenceType;
import Model.Types.StringType;
import Model.Values.BoolValue;
import Model.Values.IntValue;
import Model.Values.StringValue;
import Model.Values.Value;
import Repository.IRepository;
import Repository.Repository;
import View.Command.RunExample;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.*;
import java.io.IOException;
import java.security.PrivateKey;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ControllerPicker {
    private static IStatement compound(IStatement... statements){
        if(statements.length == 1)
            return statements[0];
        return new CompoundStatement(statements[0], compound(Arrays.copyOfRange(statements, 1, statements.length)));
    }

    private ControllerExecutor controllerExecutor;

    public void setControllerExecutor(ControllerExecutor controllerExecutor) {this.controllerExecutor = controllerExecutor;}
    @FXML
    private ListView<IStatement> programsStatesListView;

    @FXML
    private Button displayButton;

    @FXML
    private ObservableList<IStatement> getStatements() {
        List<IStatement> statementList = new ArrayList<>();
        IStatement ex1 = new CompoundStatement(new VariableDeclarationStatement("v", new IntType()),
                new CompoundStatement(new AssignmentStatement("v", new ValueExpression(new IntValue(2))),
                        new PrintStatement(new VariableExpression("v"))));
        statementList.add(ex1);

        IStatement ex2 = new CompoundStatement(new VariableDeclarationStatement("a", new IntType()),
                new CompoundStatement(new VariableDeclarationStatement("b", new IntType()),
                        new CompoundStatement(new AssignmentStatement("a", new ArithmeticExpression(new ValueExpression(new IntValue(2)), new
                                ArithmeticExpression(new ValueExpression(new IntValue(3)), new ValueExpression(new IntValue(5)), '*'), '+')),
                                new CompoundStatement(new AssignmentStatement("b", new ArithmeticExpression(new VariableExpression("a"), new ValueExpression(new
                                        IntValue(1)), '+')), new PrintStatement(new VariableExpression("b"))))));
        statementList.add(ex2);

        IStatement ex3 = new CompoundStatement(new VariableDeclarationStatement("a", new BoolType()),
                new CompoundStatement(new VariableDeclarationStatement("v", new IntType()),
                        new CompoundStatement(new AssignmentStatement("a", new ValueExpression(new BoolValue(true))),
                                new CompoundStatement(new IfStatement(new VariableExpression("a"),
                                        new AssignmentStatement("v", new ValueExpression(new IntValue(2))),
                                        new AssignmentStatement("v", new ValueExpression(new IntValue(3)))),
                                        new PrintStatement(new VariableExpression("v"))))));
        statementList.add(ex3);

        IStatement ex4 = new CompoundStatement(new VariableDeclarationStatement("varf", new StringType()),
                new CompoundStatement(new AssignmentStatement("varf", new ValueExpression(new StringValue("test.in"))),
                        new CompoundStatement(new OpenReadFile(new VariableExpression("varf")),
                                new CompoundStatement(new VariableDeclarationStatement("varc", new IntType()),
                                        new CompoundStatement(new ReadFile(new VariableExpression("varf"), "varc"),
                                                new CompoundStatement(new PrintStatement(new VariableExpression("varc")),
                                                        new CompoundStatement(new ReadFile(new VariableExpression("varf"), "varc"),
                                                                new CompoundStatement(new PrintStatement(new VariableExpression("varc")),
                                                                        new CloseReadFile(new VariableExpression("varf"))))))))));
        statementList.add(ex4);

        IStatement ex5 = new CompoundStatement(new VariableDeclarationStatement("a", new IntType()),
                new CompoundStatement(new VariableDeclarationStatement("b", new IntType()),
                        new CompoundStatement(new AssignmentStatement("a", new ValueExpression(new IntValue(5))),
                                new CompoundStatement(new AssignmentStatement("b", new ValueExpression(new IntValue(7))),
                                        new IfStatement(new RelationalExpression(new VariableExpression("a"), "<",
                                                new VariableExpression("b")), new PrintStatement(new VariableExpression("a")),
                                                new PrintStatement(new VariableExpression("b")))))));
        statementList.add(ex5);

        IStatement ex6 = new CompoundStatement(new VariableDeclarationStatement("v", new ReferenceType(new IntType())),
                new CompoundStatement(new HeapNewStatement("v", new ValueExpression(new IntValue(20))),
                        new CompoundStatement(new VariableDeclarationStatement("a", new ReferenceType(new ReferenceType(new IntType()))),
                                new CompoundStatement(new HeapNewStatement("a", new VariableExpression("v")),
                                        new CompoundStatement(new PrintStatement(new VariableExpression("v")), new PrintStatement(new VariableExpression("a")))))));
        statementList.add(ex6);


        IStatement ex7 = new CompoundStatement(new VariableDeclarationStatement("v", new ReferenceType(new IntType())),
                new CompoundStatement(new HeapNewStatement("v", new ValueExpression(new IntValue(20))),
                        new CompoundStatement(new VariableDeclarationStatement("a", new ReferenceType(new ReferenceType(new IntType()))),
                                new CompoundStatement(new HeapNewStatement("a", new VariableExpression("v")),
                                        new CompoundStatement(new PrintStatement(new HeapReadingExpression(new VariableExpression("v"))),
                                                new PrintStatement(new ArithmeticExpression(new HeapReadingExpression(
                                                        new HeapReadingExpression(new VariableExpression("a"))), new ValueExpression(new IntValue(5)), '+')))))));
        statementList.add(ex7);

        IStatement ex8 = new CompoundStatement(new VariableDeclarationStatement("v",new ReferenceType(new IntType())),
                new CompoundStatement(new HeapNewStatement("v", new ValueExpression(new IntValue(20))),
                        new CompoundStatement(new PrintStatement(new HeapReadingExpression(new VariableExpression("v"))),
                                new CompoundStatement(new HeapWritingStatement("v", new ValueExpression(new IntValue(30))),
                                        new PrintStatement(new ArithmeticExpression(new HeapReadingExpression(new VariableExpression("v")),
                                                new ValueExpression(new IntValue(5)), '+'))))));
        statementList.add(ex8);

        IStatement ex9 = new CompoundStatement(new VariableDeclarationStatement("v", new ReferenceType(new IntType())),
                new CompoundStatement(new HeapNewStatement("v", new ValueExpression(new IntValue(20))),
                        new CompoundStatement(new VariableDeclarationStatement("a", new ReferenceType(new ReferenceType(new IntType()))),
                                new CompoundStatement(new HeapNewStatement("a", new VariableExpression("v")),
                                        new CompoundStatement(new HeapNewStatement("v", new ValueExpression(new IntValue(30))),
                                                new PrintStatement(new HeapReadingExpression(new HeapReadingExpression(new VariableExpression("a")))))))));
        statementList.add(ex9);

        IStatement ex10 = new CompoundStatement(new CompoundStatement(new VariableDeclarationStatement("v", new IntType()),
                new CompoundStatement(new AssignmentStatement("v", new ValueExpression(new IntValue(4))),
                        new WhileStatement(new RelationalExpression(new VariableExpression("v"), ">",
                                new ValueExpression(new IntValue(0))), new CompoundStatement(new PrintStatement(new VariableExpression("v")),
                                new AssignmentStatement("v", new ArithmeticExpression(new VariableExpression("v"), new ValueExpression(new IntValue(1)), '-')))))), new PrintStatement(new VariableExpression("v")));
        statementList.add(ex10);

        IStatement ex11 = new CompoundStatement(new VariableDeclarationStatement("v1", new ReferenceType(new IntType())),
                new CompoundStatement(new VariableDeclarationStatement("v", new IntType()),
                new CompoundStatement(new VariableDeclarationStatement("a", new ReferenceType(new IntType())),
                        new CompoundStatement(new AssignmentStatement("v", new ValueExpression(new IntValue(10))),
                                new CompoundStatement(new HeapNewStatement("a", new ValueExpression(new IntValue(22))),
                                        new CompoundStatement(new ForkStatement(new CompoundStatement(new HeapWritingStatement("a", new ValueExpression(new IntValue(30))),
                                                new CompoundStatement(new AssignmentStatement("v", new ValueExpression(new IntValue(32))),
                                                        new CompoundStatement(new PrintStatement(new VariableExpression("v")), new CompoundStatement(new PrintStatement(new HeapReadingExpression(new VariableExpression("a"))), new HeapNewStatement("v1", new ValueExpression(new IntValue(59)))))))),
                                                new CompoundStatement(new PrintStatement(new VariableExpression("v")),
                                                        new CompoundStatement(new PrintStatement(new HeapReadingExpression(new VariableExpression("a"))),
                                                                new CompoundStatement(new NopStatement(), new CompoundStatement(new NopStatement(), new CompoundStatement(new NopStatement(), new NopStatement())))))))))));
        statementList.add(ex11);

        IStatement ex12 = new CompoundStatement(new VariableDeclarationStatement("a", new ReferenceType(new IntType())),
                                                new CompoundStatement(new VariableDeclarationStatement("b", new ReferenceType(new IntType())),
                                                                      new CompoundStatement(new VariableDeclarationStatement("v", new IntType()),
                                                                                            new CompoundStatement(new HeapNewStatement("a", new ValueExpression(new IntValue(0))),
                                                                                                                  new CompoundStatement(new HeapNewStatement("b", new ValueExpression(new IntValue(0))),
                                                                                                                                        new CompoundStatement(new HeapWritingStatement("a", new ValueExpression(new IntValue(1))),
                                                                                                                                                              new CompoundStatement(new HeapWritingStatement("b", new ValueExpression(new IntValue(2))),
                                                                                                                                                                                    new CompoundStatement(new ConditionalAssignmentStatement("v", new RelationalExpression(new HeapReadingExpression(new VariableExpression("a")), "<", new HeapReadingExpression(new VariableExpression("b"))), new ValueExpression(new IntValue(100)), new ValueExpression(new IntValue(200))),
                                                                                                                                                                                                          new CompoundStatement(new PrintStatement(new VariableExpression("v")),
                                                                                                                                                                                                                                new CompoundStatement(new ConditionalAssignmentStatement("v", new RelationalExpression(new ArithmeticExpression(new HeapReadingExpression(new VariableExpression("a")), new ValueExpression(new IntValue(2)), '-'), ">", new HeapReadingExpression(new VariableExpression("a"))), new ValueExpression(new IntValue(100)), new ValueExpression(new IntValue(200))),
                                                                                                                                                                                                                                                      new PrintStatement(new VariableExpression("v"))))))))))));
        statementList.add(ex12);

        IStatement ex13 = new CompoundStatement(new VariableDeclarationStatement("v1", new ReferenceType(new IntType())),
                                                new CompoundStatement(new VariableDeclarationStatement("v2", new ReferenceType(new IntType())),
                                                                      new CompoundStatement(new VariableDeclarationStatement("v3", new ReferenceType(new IntType())),
                                                                                            new CompoundStatement(new VariableDeclarationStatement("cnt", new IntType()),
                                                                                                                  new CompoundStatement(new HeapNewStatement("v1", new ValueExpression(new IntValue(2))),
                                                                                                                                        new CompoundStatement(new HeapNewStatement("v2", new ValueExpression(new IntValue(3))),
                                                                                                                                                              new CompoundStatement(new HeapNewStatement("v3", new ValueExpression(new IntValue(4))),
                                                                                                                                                                                    new CompoundStatement(new NewLatchStatement("cnt", new HeapReadingExpression(new VariableExpression("v2"))),
                                                                                                                                                                                                          new CompoundStatement(new ForkStatement(new CompoundStatement(new HeapWritingStatement("v1", new ArithmeticExpression(new HeapReadingExpression(new VariableExpression("v1")), new ValueExpression(new IntValue(10)), '*')),
                                                                                                                                                                                                                                                                        new CompoundStatement(new PrintStatement(new HeapReadingExpression(new VariableExpression("v1"))),
                                                                                                                                                                                                                                                                                              new CompoundStatement(new CountDownStatement("cnt"),
                                                                                                                                                                                                                                                                                                                    new ForkStatement(new CompoundStatement(new HeapWritingStatement("v2", new ArithmeticExpression(new HeapReadingExpression(new VariableExpression("v2")), new ValueExpression(new IntValue(10)), '*')),
                                                                                                                                                                                                                                                                                                                                                            new CompoundStatement(new PrintStatement(new HeapReadingExpression(new VariableExpression("v2"))),
                                                                                                                                                                                                                                                                                                                                                                                  new CompoundStatement(new CountDownStatement("cnt"),
                                                                                                                                                                                                                                                                                                                                                                                                        new ForkStatement(new CompoundStatement(new HeapWritingStatement("v3", new ArithmeticExpression(new HeapReadingExpression(new VariableExpression("v3")), new ValueExpression(new IntValue(10)), '*')),
                                                                                                                                                                                                                                                                                                                                                                                                                                                new CompoundStatement(new PrintStatement(new HeapReadingExpression(new VariableExpression("v3"))),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                      new CountDownStatement("cnt")))))))))))),
                                                                                                                                                                                                                                new CompoundStatement(new AwaitStatement("cnt"),
                                                                                                                                                                                                                                                      new CompoundStatement(new PrintStatement(new ValueExpression(new IntValue(100))),
                                                                                                                                                                                                                                                                            new CompoundStatement(new CountDownStatement("cnt"),
                                                                                                                                                                                                                                                                                                  new PrintStatement(new ValueExpression(new IntValue(100)))))))))))))));

        statementList.add(ex13);

        return FXCollections.observableArrayList(statementList);
    }

    @FXML
    private void displayProgram(ActionEvent actionEvent) {
        IStatement selectedStatement = programsStatesListView.getSelectionModel().getSelectedItem();
        if (selectedStatement == null) {
            Alert alert = new Alert(Alert.AlertType.ERROR);
            alert.setTitle("Error encountered!");
            alert.setContentText("There was no statement selected!");
            alert.showAndWait();
        } else {
            int id = programsStatesListView.getSelectionModel().getSelectedIndex();
            try {
                selectedStatement.typeCheck(new MyDict<>());
                ProgramState programState = new ProgramState(selectedStatement);
                IRepository repository = new Repository(programState, "log" + (id + 1) + ".txt");
                repository.emptyLogFile();
                Controller controller = new Controller(repository);
                controllerExecutor.setController(controller);
            } catch (Exception exception) {
                Alert alert = new Alert(Alert.AlertType.ERROR);
                alert.setTitle("Error encountered!");
                alert.setContentText(exception.getMessage());
                alert.showAndWait();
            }
        }
    }

    @FXML
    protected void initialize() {
        programsStatesListView.setItems(getStatements());
        programsStatesListView.getSelectionModel().setSelectionMode(SelectionMode.SINGLE);
    }
}