
public class Fibonacci {
    
    // Fibonacci Recursive Inefficient Version
    public static int fib(int n){
        if(n < 1){
            return 0;
        }
        if(n == 1 || n == 2){
            return 1;
        }
        return fib(n-1) + fib(n-2);
    }
    
    // Fibonacci Recursive Dinamic Programming Top-down
    public static int fib(int n, Integer[] mem){
        if(n < 1){
            return 0;
        }
        if(mem[n] == null){
            if(n == 1 || n == 2){
                mem[n] = 1;
            }
            mem[n] = fib(n-1, mem) + fib(n-2, mem);
        }
        return mem[n];
    }
    
    // Fibonacci Dinamic Programming Bottom-up
    public static int fib2(int n, Integer[] mem){
        if(n < 1) {
            return 0;
        }
        if(n == 1 || n == 2){
            return 1;
        }
        mem[1] = 1;
        mem[2] = 1;
        for(int i = 3; i <= n; i++){
            mem[i] = mem[i-1] + mem[i-2];
        }
        return mem[n];
    }
    

}
