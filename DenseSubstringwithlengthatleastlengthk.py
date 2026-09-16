def solve(s,k):
    n = len(s)
    pref = [0 for i in range(n+1)]
    
    for i in range(1,n+1):
        pref[i] = -1 if(s[i-1] == '0') else 1
        pref[i] = pref[i]+pref[i-1]
    mini = pref[0]
    
    for i in range(k,n+1):
       
        if(pref[i]-mini>0):
            return True
        mini = min(mini,pref[i-k+1])
    return False
s = "000001"
k = 1
print(solve(s,k))