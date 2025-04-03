class Node {
    int data;
    Node left, right;
    Node(int item) {
        data = item;
        left = right = null;
    }
}
public class TreeImplement {
    Node root;

    // Constructor
    public inseart(int x){
        if (root == null){
            root = new Node(x);
            return;
        }
        Node t = root, prev = null;
        while (t!= null) {
            prev = t;
            if (x < t.data)
                t = t.left;
            else
                t = t.right;
        }
    }

}
