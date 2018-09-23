function solution(A) {
    // write your code in JavaScript (Node.js 8.9.4)
    // Sort the array
    A.sort((a, b)=>a-b);
    let digit;
    let server1, server2;
    server1 = 0;
    server2 = 0;
    while(A.length > 0){
        digit = A.pop();
        // Decide where to put the digit
        if (Math.abs(server1 + digit - server2)  <= Math.abs(server2 + digit - server1)) {
            server1 += digit;
        }else{
            server2 += digit;
        }
    }
    return Math.abs(server1-server2);
}

A = [123,2,3,5,4556,7,8,5,3,12313,443];
console.log(solution(A));