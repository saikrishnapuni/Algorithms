def solve(s,k):
    sumi = 0
    n = len(s)
    for i in range(0,k):
        if(s[i] == '1'):
            sumi+=1
        else:
            sumi-=1
    if(sumi>0):
        return True
    for i in range(k,n):
        if(s[i] == '1'):
            sumi+=1
        else:
            sumi-=1
        if(s[i-k] == '0'):
            sumi+=1
        else:
            sumi-=1
        if(sumi>0):
            return True
    return False
S = "00111010"
k = 4
print(solve(S,k))