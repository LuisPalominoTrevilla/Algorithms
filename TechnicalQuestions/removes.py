def remove(A,n):
    pos = n-1
    pos%=len(A)
    while(len(A)>1):
        A.pop(pos)
        pos+=n-1
        pos%=len(A)
    return A[0]
x = [1,2,3]
print(remove(x, 4))