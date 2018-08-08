import java.util.Random;

public class QuickSelect {
    
    /**
     *  Main quick select method
     * @param k
     * @param arr
     * @return
     */
    public static Integer quickSelect(int k, Integer[] arr) {
        return quickSelect(arr, --k, 0, arr.length-1);
    }
    
    /**
     *  Helper method to make quickselect recursive
     * @param arr
     * @param k
     * @param low
     * @param high
     * @return
     */
    public static Integer quickSelect(Integer[] arr, int k, int low, int high){
        if(high == low) return arr[low];
        int pivot_location = partition(arr, low, high);
        if(pivot_location == k){
            return arr[k];
        }else if (pivot_location > k){
            return quickSelect(arr, k, low, pivot_location-1);
        }else{
            return quickSelect(arr, k, pivot_location+1, high);
        }
    }
    
    /**
     *  Partitions array to the right and left from randomly chosen pivot
     * @param arr
     * @param low
     * @param high
     * @return
     */
    public static int partition(Integer[] arr, int low, int high){
        Random r = new Random();
        int pivot_index = r.nextInt(high - low + 1) + low;
        Integer aux = arr[pivot_index];
        arr[pivot_index] = arr[high];
        arr[high] = aux;
        
        Integer pivot = arr[high];
        int i = low;
        int j = high;
        Integer[] C = new Integer[arr.length];
        
        for(int k = low; k < high; k++){
            if(arr[k].compareTo(pivot) < 0){
                C[i++] = arr[k];
            }else{
                C[j--] = arr[k];
            }
        }
        C[i] = pivot;  // Copy the pivot
        
        // Copy content from C to arr
        for(int index = 0; index < arr.length; index++){
            
            if(C[index] != null){
                arr[index] = C[index];
            }
        }
        return i;
    }
    
}
