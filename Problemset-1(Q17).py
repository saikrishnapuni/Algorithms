# Rabin Karp Algorithm

# Given a string text and a string pattern, implement the Rabin-Karp algorithm to find the starting index of all occurrences of pattern in text. If pattern is not found, return an empty list.


# Example 1

# Input: text = "ababcabcababc", pattern = "abc"



# Output: [2, 5, 10]



# Expalanation : The pattern "abc" is found at indices 2, 5, and 10 in the text.

# Example 2

# Input: text = "hello", pattern = "ll"



# Output: [2]



# Explanation: The pattern "ll" is found at index 2 in the text.


MOD = 10**9 + 7
def solve(s,p):
    d = 256
    z = 1
    x = 0
    y = 0
    n = len(p)
    m = len(s)
    if(m<n):
        return []
    ans = []
    for  i in range(0,n):
        z = (z*256)%MOD
        x = (x*256 + ord(p[i]))%MOD
        y = (y*256 + ord(s[i]))%MOD
    if(x == y):
        for i in range(0,n):
            if(s[i] != p[i]):
                break
        else:
            ans.append(0)
    for k in range(n,m):
        y = ((y*256 + ord(s[k])) - (z*ord(s[k-n])))%MOD
        if(y<0):
            y= y+MOD
        if(x == y):
            if(s[k-n+1:k+1] == p):
                ans.append(k-n+1)
    return ans
text = "ababcabcababc"
pattern = "abc"
text = "abcdef"
pattern = "gh"
text = "hello"
pattern = "ll"
print(solve(text,pattern))