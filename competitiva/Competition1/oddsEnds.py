def oddsEnds(sequence, n):
    if sequence[0]%2==0 or sequence[n-1]%2==0 or n%2==0:
        print("NO")
    else:
        print("YES")
n = int(input())
sequence = [int(x) for x in input().split()]
oddsEnds(sequence, n)