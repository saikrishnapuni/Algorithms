# Next Question

# Given a binary string of length \(n\), design a linear-time \(O(n)\) algorithm to compute the length of the largest substring containing an equal number of 0s and 1s.
def solve(s):
    d = {0:-1}
    sumi = 0
    n = len(s)
    maxi = 0
    for i in range(0,n):
        if(s[i] == '0'):
            sumi-=1
        else:
            sumi+=1
        if(sumi in d):
            maxi = max(maxi,i-d[sumi])
        else:
            d[sumi] = i
    return maxi    
print(solve("00101101"))