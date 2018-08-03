import java.util.Arrays;

public class MergeSort {
    
    public MergeSort(Integer[] arr){
        mergeSort(arr, 0, arr.length-1);
    }
    
    public void mergeSort(Integer[] arr, int low, int high){
        // Base case
        if(high - low <= 0) return;
        int mid = (low + high)/2;
        mergeSort(arr, low, mid);
        mergeSort(arr, mid+1, high);
        Integer[] A = Arrays.copyOfRange(arr, low, mid+1);
        Integer[] B = Arrays.copyOfRange(arr, mid+1, high+1);
        Integer[] aux = merge(A, B);
        int j = 0;
        for(int i = low; i <= high; i++){
            arr[i] = aux[j++];
        }
    }
    
    public Integer[] merge(Integer[] a, Integer[] b){
        Integer[] C = new Integer[a.length + b.length];
        int i = 0;
        int j = 0;
        int k = 0;
        
        // Place values from arrays a and b to array C
        while(i < a.length && j < b.length){
            C[k++] = (a[i].compareTo(b[j]) < 0)? a[i++]:b[j++];
        }
        
        // Move last values from a or b to array C
        while(i < a.length){
            C[k++] = a[i++];
        }
        while(j < b.length){
            C[k++] = b[j++];
        }
        return C;
    }
    
    public static void main(String[] args) {
        Integer[] a = {new Integer(7), new Integer(2), new Integer(1), new Integer(6)};

        new MergeSort(a);
        for(Integer x: a){
            System.out.print(x.intValue() + ", ");
        }
    }

}
