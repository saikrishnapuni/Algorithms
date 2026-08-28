# Question

# Given a binary string of length \(n\), design a linear-time \(O(n)\) algorithm to compute the length of the largest dense substring, where a dense substring has more 1s than 0s.
def longest(s):
    n  = len(s)
    # pref = [0 for i in range(n+1)]
    # for i in range(1,n+1):
    #     if(s[i-1] == '0'):
    #         pref[i] = pref[i-1]-1
    #     else:
    #         pref[i] = pref[i-1]+1
    
    # # mini = 0
    # # #brute force
    # # for i in range(1,n+1):
    # #     for j in range(0,i):   
    # #         if(pref[i]>pref[j]):
    # #             mini = max(mini,i-j)
    # #             break
    
    
    # # return mini
    
    d = {}
    sumi = 0
    maxln = 0
    for i in range(0,n):
        if(s[i] == '0'):
            sumi-=1
        else:
            sumi+=1
        if(sumi>0):
            maxln = max(maxln,i+1)
        else:
            if((sumi-1) in d):
                maxln = max(maxln,i-d[sumi-1])
        if(sumi not in d):
            d[sumi] = i
    return maxln
    
        
    
print(longest("1000111"))