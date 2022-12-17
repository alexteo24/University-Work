package LinkedList;

public class LinkedList<T> {
    private Node head;
    private class Node {
        private T data;
        private Node next;

        public Node(T data) {
            this.data = data;
            this.next = null;
        }
    }
    private String stringForm;

    public LinkedList() {
        head = null;
        stringForm = "";
    }

    public void add(T data) {
        if (head == null) {
            head = new Node(data);
            return;
        }
        Node currentNode = head;
        while(currentNode.next != null) {
            currentNode = currentNode.next;
        }
        currentNode.next = new Node(data);
    }

    public String displayList() {
        Node currentNode = head;
        while (currentNode != null) {
            stringForm += currentNode.data + "\n";
            currentNode = currentNode.next;
        }
        return stringForm;
    }
}
