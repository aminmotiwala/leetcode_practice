package org.example;

import java.util.*;

public class MinHeapImplementation {
    Integer[] data;
    Integer noe;

    public MinHeap(){
        data = new Integer[10];
        noe = 0;
    }

    public Integer peek(){
        return data[0];
    }

    public void push(Integer newRecord){
        if (noe == 10) {
            System.out.println("Max size reached sorry.");
            return;
        }
        // insert will be at the end
        Integer insertIndex = noe;
        data[insertIndex] = newRecord;
        Integer parentIndex = (insertIndex - 1)/ 2;
        while (parentIndex >= 0 && data[parentIndex] > newRecord){
            //swap
            Integer temp = data[parentIndex];
            data[parentIndex] = newRecord;
            data[insertIndex] = temp;
        }
        noe++;
    }

    public Integer pop(){
        if (noe == 0){
            System.out.println("EMPTY");
            return 0;
        }
        Integer toReturn = data[0];
        noe--;
        // put last object at the beginning
        data[0] = data[noe];
        //reset last object
        data[noe] = null;
        // decrement number of elements


        // now we need to sort the heap
        // we will look at children if children smaller than parent and which child is smaller replace
        Integer sortingBeganIndex = 0;
        Integer child1IndexIndex = 1;
        Integer child2IndexIndex = 2;

        //TODO REFACTOR THIS FOR BETTER HANDLING
        // if both child present
        if (!Objects.isNull(data[child1IndexIndex]) && !Objects.isNull(data[child2IndexIndex])) {
            while ((child1IndexIndex <= noe-1) && (child2IndexIndex <= noe-1) && data[sortingBeganIndex] > Math.min(data[child1IndexIndex], data[child2IndexIndex])){
                if (data[child1IndexIndex] < data[child2IndexIndex]){

                    Integer temp = data[sortingBeganIndex];
                    data[sortingBeganIndex] = data[child1IndexIndex];
                    data[child1IndexIndex]= temp;
                    sortingBeganIndex = child1IndexIndex;

                }else {

                    Integer temp = data[sortingBeganIndex];
                    data[sortingBeganIndex] = data[child2IndexIndex];
                    data[child2IndexIndex]= temp;
                    sortingBeganIndex= child2IndexIndex;
                }

                child1IndexIndex = 2*sortingBeganIndex+1;
                child2IndexIndex = 2*sortingBeganIndex+2;
            }
        } else if(!Objects.isNull(data[child1IndexIndex])) {
            while (data[sortingBeganIndex] > data[child1IndexIndex]){

                Integer temp = data[sortingBeganIndex];
                data[sortingBeganIndex] = data[child1IndexIndex];
                data[child1IndexIndex]= temp;
                sortingBeganIndex= child1IndexIndex;
            }
        }else if (!Objects.isNull(data[child2IndexIndex])){
            while (data[sortingBeganIndex] > data[child2IndexIndex]){
                Integer temp = data[sortingBeganIndex];
                data[sortingBeganIndex] = data[child2IndexIndex];
                data[child2IndexIndex]= temp;
                sortingBeganIndex= child2IndexIndex;
            }
        }


        return toReturn;
    }

    public static void main(String[] args) {
        MinHeap t = new MinHeap();
        t.push(2);
        t.push(1);
        t.push(2);
        t.push(5);
        t.peek();
        System.out.println(t.pop());
        System.out.println(t.pop());


    }

}
