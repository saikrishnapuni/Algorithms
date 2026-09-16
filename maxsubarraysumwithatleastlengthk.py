# def solve(arr,k):
#     n = len(arr)
#     pref = [0 for i in range(n)]
#     pref[0] = arr[0]
#     for i in range(1,n):
#         pref[i] = pref[i-1]+arr[i]
#     maxi = float("-inf")
#     mini = float("inf")
#     for i in range(k-1,n):
#         maxi = max(pref[i],maxi)
#         if(i-k>=0):
#             mini = min(mini,pref[i-k])
#             maxi = max(pref[i]-mini,maxi)
        
#     return maxi

#O(1) space

def solve(arr,k):
    sumi = 0
    n = len(arr)
    for i in range(0,k):
        sumi+=arr[i]
    maxi = sumi
    mini = 0
    pref = 0
    for i in range(k,n):
        pref +=arr[i-k]
        mini = min(mini,pref)
        sumi+=arr[i]
        maxi = max(maxi,sumi-mini)
    return maxi
print(solve([2, -1, 3, 4, -2, 5],3))