#Maximum Profit from a Single Stock Transaction
# Let 𝑃[0…𝑛-1] represent the price of a stock over 𝑛 days. Design a linear time algorithm to determine the maximum profit obtainable from exactly one buy-sell transaction under each of the following conditions:

# The stock must be sold after it is bought.

def solve(arr):
    n = len(arr)
    maxi = float("-inf")
    mini = arr[0]
    for i in range(1,n):
        maxi = max(maxi,arr[i]-mini)
        mini = min(arr[i],mini)
    return maxi

#The stock must be sold exactly 𝑘 days after it is bought.

def solve(arr,k):
    n = len(arr)
    maxi = float("-inf")
    
    for i in range(k,n):
        maxi = max(maxi,arr[i]-arr[i-k])
    return maxi

#The stock must be sold at least 𝑘 days after it is bought.

def solve(arr,k):
    n = len(arr)
    maxi = arr[k]-arr[0]
    mini = arr[0]
    for i in range(k+1,n):
        maxi = max(maxi,arr[i]-mini)
        mini = min(mini,arr[i-k])
    return maxi

#The stock must be sold at most 𝑘 days after it is bought.
from collections import deque
def solve(arr,k):
    n = len(arr)
    stk = deque([0])
    maxi = 0
    for i in range(1,n):
        while(stk and i-stk[0]>k):
            stk.popleft()
        maxi = max(maxi,arr[i]-arr[stk[0]])
        while(stk and arr[stk[-1]]>=arr[i]):
            stk.pop()
        stk.append(i)
    return maxi
    
# Part B: Maximum-Sum Subarrays with Length Constraints


# Let 𝐴[0…𝑛-1] be a sequence of numbers. Design a linear time algorithm to find a maximum-sum contiguous subarray under each of the following conditions:

# The subarray length is unrestricted.

def solve(arr):
    n = len(arr)
    sumi = 0
    maxi = float("-inf")
    for i in arr:
        sumi+=i
        maxi = max(maxi,sumi)
        if(sumi<0):
            sumi = 0
    return maxi

#The subarray length is exactly k.

def solve(arr,k):
    n = len(arr)
    sumi = 0
    maxi = float("-inf")
    for i in range(0,k):
        sumi+=arr[i]
    maxi = max(maxi,sumi)
    for i in range(k,n):
        sumi-=arr[i-k]
        sumi+=arr[i]
        maxi = max(maxi,sumi)
    return maxi

#The subarray length is at least k.

def solve(arr,k):
    n = len(arr)
    pref = [0 for i in range(n+1)]
    for i in range(1,n+1):
        pref[i] = pref[i-1]+arr[i-1]
    maxi = pref[k]-pref[0]
    mini = pref[0]
    for i in range(k+1,n+1):
        mini = min(mini,pref[i-k])
        maxi = max(maxi,pref[i]-mini)
        
    return maxi

#The subarray length is at most 𝑘.

from collections import deque
def solve(arr,k):
    if(k == 1):
        return max(arr)
    n = len(arr)
    pref = [0 for i in range(n+1)]
    for i in range(1,n+1):
        pref[i] = pref[i-1]+arr[i-1]
    stk = deque([0])
    maxi = float("-inf")
    for i in range(1,n+1):
        while(stk and i-stk[0]>k):
            stk.popleft()
        maxi = max(maxi,pref[i]-pref[stk[0]])
        while(stk and pref[stk[-1]]>=pref[i]):
            stk.pop()
        stk.append(i)
    return maxi

# Part C: Dense Substrings in a Binary String
# Let 𝑆 be a binary string of length 𝑛. Design a linear time algorithm to determine whether S contains a dense substring satisfying each of the following conditions:

# The substring length is exactly 𝑘.

#1>#0
def solve(s,k):
    n = len(s)
    pref = [0 for i in range(n+1)]
    for i in range(1,n+1):
        pref[i] = pref[i-1]
        if(s[i-1] == '0'):
            pref[i]-=1
        else:
            pref[i]+=1
    for i in range(k,n+1):
        if(pref[i]-pref[i-k]>0):
            return True
    return False

#The substring length is at least 𝑘.

def solve(s,k):
    n = len(s)
    pref = [0 for i in range(n+1)]
    for i in range(1,n+1):
        pref[i] = pref[i-1]
        if(s[i-1] == '0'):
            pref[i]-=1
        else:
            pref[i]+=1
    mini = pref[0]
    if(pref[k]-pref[0]>0):
        return True
    for i in range(k+1,n+1):
        if(pref[i]-mini>0):
            return True
        mini = min(mini,pref[i-k])
    return False

#The substring length is between 𝑘 and 𝑙, inclusive.

from collections import deque

def solve(s, k, l):
    n = len(s)
    pref = [0 for i in range(n + 1)]

    for i in range(1, n + 1):
        pref[i] = -1 if s[i - 1] == '0' else 1
        pref[i] += pref[i - 1]

    stk = deque()

    for i in range(k, n + 1):

        while stk and stk[0] < i - l:
            stk.popleft()

        
        j = i - k
        while stk and pref[stk[-1]] > pref[j]:
            stk.pop()
        stk.append(j)

        
        if pref[i] - pref[stk[0]] > 0:
            return True

    return False

