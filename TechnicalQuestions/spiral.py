def spiralPrint(m):
    i, j = 0,0
    maxj,minj,maxi,mini = len(m[0]), 0, len(m), 1
    cont = 1
    res = str(m[i][j])+" "
    while cont < len(m)*len(m[0]):
        while j+1 < maxj:
            j+=1
            cont+=1
            res += str(m[i][j])+" "
        maxj-=1
        while i+1 < maxi:
            i+=1
            cont+=1
            res += str(m[i][j]) + ' '
        maxi-=1
        while j-1 >= minj:
            j-=1
            cont+=1
            res += str(m[i][j])+" "
        minj+=1
        while i-1 >= mini:
            i-=1
            cont+=1
            res += str(m[i][j]) + ' '
        mini+=1
    print(res)

m = [[1,2,3,4,5,6,7,8,9],
     [10,11,12,13,14,15,16,17,18],
     [19,20,21,22,23,24,25,26,27,],
     [28,29,30,31,32,33,34,35,36]]
a = [[1,2,3],
     [4,5,6],
     [7,8,9]]
spiralPrint(m)