package org.example;

import java.util.HashMap;
import java.util.Map;

public class LRUCache<T> {
    private final int size;
    private Map<T, Node> data;

    private Node head;
    private Node tail;

    public LRUCache(int size){
        this.size = size;
        this.data = new HashMap<>();

        head = new Node();
        tail= new Node();
        head.next = tail;
        tail.previous = head;
    }

    public void printData(){
        System.out.println("====== MAP =====");
        for (T d : data.keySet()){
            System.out.print(d.toString()+" ");
        }

        System.out.println("====== List =====");
        Node currentHead = head;
        while (currentHead.next != null){
            System.out.print(currentHead.value != null ? currentHead.value .toString() : "" +" -> ");
            currentHead = currentHead.next;
        }
    }
    public void put(T value){
        // first check if not in map and less than capacity
        Node newData = new Node();
        newData.value = value;

        if (!data.containsKey(value) && data.size() < size){
            addDataToList(newData);
            data.put(value, newData);
        }else if(data.containsKey(value)){
            removeDataFromList(newData);
            addDataToList(newData);
        } else if (data.size() == size) {
            Node nodeToDelete = tail.previous;
            removeNodeFromTail(tail.previous);
            addDataToList(newData);
            data.remove(nodeToDelete.value);
            data.put(value, newData);
        }


    }

    private void addDataToList(Node newData) {
        newData.next = head.next;
        newData.previous = head;

        head.next.previous = newData;
        head.next = newData;
    }

    private void removeDataFromList(Node newData) {
        Node currentHead = head;
        while (currentHead.next != null){
            if (currentHead.value == newData.value){
                removeNodeFromTail(currentHead);
                currentHead.next = null;
                currentHead.previous = null;
                break;
            }
            currentHead = currentHead.next;
        }
    }
    private void removeNodeFromTail(Node nodeToDelete){
        nodeToDelete.previous.next = nodeToDelete.next;
        nodeToDelete.next.previous = nodeToDelete.previous;
    }

    class Node{
        T value;
        Node next;
        Node previous;
    }

    public static void main(String[] args) {
        LRUCache<String> aminCache = new LRUCache(3);
        aminCache.put("amin");
        aminCache.put("umair");
        aminCache.put("usman");
        aminCache.put("amin");
        aminCache.put("ali");
        aminCache.printData();
    }
}
