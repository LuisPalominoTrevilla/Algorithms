def proveDivisible(n):
    if int(n)%8 == 0:
        return 'YES\n'+n
    for i in range(len(n)):
        if int(n[i])%8 == 0:
            return 'YES\n'+n[i]
        for j in range(i+1,len(n)):
            if int(n[i]+n[j])%8 == 0:
                return 'YES\n'+n[i]+n[j]
            for k in range(j+1, len(n)):
                if int(n[i]+n[j]+n[k])%8 == 0:
                    return 'YES\n'+n[i]+n[j]+n[k]
    return 'NO'
n = str(input())
print(proveDivisible(n))