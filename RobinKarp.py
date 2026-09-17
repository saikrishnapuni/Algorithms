def solve(text,pat):
    mod = 10**9 + 7
    n1 = len(text)
    n2 = len(pat)
    if(n1<n2):
        return -1
    x = 0
    y = 0
    z = 1
    for i in range(0,n2):
        z = (z*256)%mod
        y = (y*256+ord(pat[i]))%mod
        x = (x*256+ord(text[i]))%mod
    if(x == y):
        if(pat == text[:n2]):
            return 0
    for i in range(n2,n1):
        x = (x*256+ord(text[i]) - z*ord(text[i-n2]))%mod
        if(x<0):
            x = x+mod
        if(x == y):
            if(text[i-n2+1:i+1] == pat):
                return i-n2+1
    return -1
text = "ababcabcababc"
pattern = "abc"
print(solve(text,pattern))