package BinarySearchTree;

public class BST<T extends Comparable<T>> {
    private class Node {
        private Node left, right;
        private T data;

        public Node(T data) {
            this.data = data;
        }

    }

    private Integer length;
    private Node head;
    private String stringForm;

    public BST() {
        head = null;
        length = 0;
        stringForm = "";
    }


    public Integer getLength() {
        return length;
    }


    public void add(T data) {
        if (find(data) != null) {
            return;
        }
        length++;
        if (head == null) {
            head = new Node(data);
            return;
        }
        Node currentNode = head;
        while (true) {
            if (data.compareTo(currentNode.data) < 0) {
                if (currentNode.left == null) {
                    currentNode.left = new Node(data);
                    break;
                } else {
                    currentNode = currentNode.left;
                }
            } else {
                if (currentNode.right == null) {
                    currentNode.right = new Node(data);
                    break;
                } else {
                    currentNode = currentNode.right;
                }
            }
        }
    }

    public T find(T data) {
        Node currentNode = head;
        while (currentNode != null) {
            if (currentNode.data.compareTo(data) == 0) {
                return data;
            }
            if (data.compareTo(currentNode.data) < 0) {
                currentNode = currentNode.left;
            } else {
                currentNode = currentNode.right;
            }
        }
        return null;
    }


    private void print(Node currentNode) {
        if (currentNode == null) {
            return;
        }
        print(currentNode.left);
        stringForm += currentNode.data + "\n";
        print(currentNode.right);
    }

    public String displayTree() {
        print(head);
        return stringForm;
    }
}
