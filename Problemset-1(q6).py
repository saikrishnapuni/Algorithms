# Question 9

# Given a binary string \(S\) of length \(n\), design a linear-time algorithm to compute \(k\), such that:

# $$ \text{number of 0's in } S[0..k] = \text{number of 1's in } S[k+1..n-1] $$

# Write your code and paste it here.

def solve(s):
    c = 0
    n = len(s)
    for i in s:
        if(i == '1'):
            c+=1
    if(c == 0):
        return -1
    if(c == n):
        return n-1
    return c-1
print(solve("01011010"))