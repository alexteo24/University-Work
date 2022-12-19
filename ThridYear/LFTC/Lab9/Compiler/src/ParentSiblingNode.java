public class ParentSiblingNode {
    private String info;
    private Integer parent;
    private Integer rightSibling;

    public ParentSiblingNode(String info, Integer parent, Integer rightSibling) {
        this.info = info;
        this.parent = parent;
        this.rightSibling = rightSibling;
    }

    public String getInfo() {
        return info;
    }

    public void setInfo(String info) {
        this.info = info;
    }

    public Integer getParent() {
        return parent;
    }

    public void setParent(Integer parent) {
        this.parent = parent;
    }

    public Integer getRightSibling() {
        return rightSibling;
    }

    public void setRightSibling(Integer rightSibling) {
        this.rightSibling = rightSibling;
    }

    @Override
    public String toString() {
        return "ParentSiblingNode{" +
                "info='" + info + '\'' +
                ", parent=" + parent +
                ", rightSibling=" + rightSibling +
                '}';
    }
}
