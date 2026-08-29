# Question — Rank Queries on a Set of Integer Intervals

# Given n integer intervals [Lᵢ, Rᵢ], design a data structure that represents the union of all intervals and supports the following operations efficiently:

# Merge overlapping or adjacent intervals into disjoint intervals.
# Given an integer x, find its rank among all integers contained in the union of the intervals, where rank 1 is the largest element.
# Given an integer k, find the element having rank k (the k-th largest integer) in the union.
# Handle intervals with arbitrary ordering of endpoints (L > R should also be allowed).
# If x or k is outside the represented set, handle it appropriately.

def solve(arr,k):
    n = len(arr)
    arr.sort()
    ans = []
    prev = arr[0]
    for i in range(1,n):
        if(arr[i][0]<=prev[1]+1):
            prev[1] = max(prev[1],arr[i][1])
        else:
            ans.append(prev)
            prev = arr[i]
    ans.append(prev)
    n = len(ans)
    suff = [0 for i in range(n)]
    for i in range(n-1,-1,-1):
        length = ans[i][1]-ans[i][0]+1
        if(i == n-1):
            suff[i] = length
        else:
            suff[i] = length+suff[i+1]
    kind = n-1
    for i in range(0,n-1):
        if(k>suff[i+1] and k<=suff[i]):
            kind = i
            break
    if(kind<n-1):
        k = k-suff[kind+1]
    
    
    h =  ans[kind][1]
    return h-k+1
    
