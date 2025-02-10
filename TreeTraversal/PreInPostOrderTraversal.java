package org.example;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class PreInPostOrderTraversal {

    // Initialize Tree for further operations
    public TreeNode initializeTree(){
        TreeNode root = new TreeNode();
        root.value = "D";
        root.left = new TreeNode();
        root.left.value = "B";
        root.right = new TreeNode();
        root.right.value = "G";
        root.left.left = new TreeNode();
        root.left.left.value = "A";
        root.left.right = new TreeNode();
        root.left.right.value = "C";
        root.right.left = new TreeNode();
        root.right.left.value = "F";
        return root;
    }

    public static void main(String[] args) {
        PreInPostOrderTraversal traversing = new PreInPostOrderTraversal();
        TreeNode rode =  traversing.initializeTree();
        traversing.postOrderRecursive(rode);
    }

    // d -> g -> b -> c -> a

    public void preOrder(TreeNode root){
        Stack<TreeNode> nodeStack = new Stack<>();
        nodeStack.push(root);

        while (!nodeStack.isEmpty()) {
            TreeNode currentNode = nodeStack.pop();
            System.out.print(currentNode.value+"->");
            if (currentNode.right != null) {
                nodeStack.push(currentNode.right);
            }
            if (currentNode.left != null){
                nodeStack.push(currentNode.left);
            }

        }

    }

    public void preOrderRecursive(TreeNode root){

        if (root == null){
            return;
        }

        System.out.println(root.value);
        preOrderRecursive(root.left);
        preOrderRecursive(root.right);

    }

    public void inOrderRecursive(TreeNode root){
        if (root == null){
            return;
        }
        inOrderRecursive(root.left);
        System.out.println(root.value);
        inOrderRecursive(root.right);
    }

    public void postOrderRecursive(TreeNode root){
        if (root == null){
            return;
        }
        postOrderRecursive(root.left);
        postOrderRecursive(root.right);
        System.out.println(root.value);
    }
}

class TreeNode{
    String value;
    TreeNode left;
    TreeNode right;
}
