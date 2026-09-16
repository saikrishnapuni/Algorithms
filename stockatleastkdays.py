def solve(arr,k):
    maxi = float("-inf")
    mini = float("inf")
    for i in range(k,len(arr)):
        mini = min(mini,arr[i-k])
        maxi = max(maxi,arr[i]-mini)
    return maxi

print(solve([10, 2, 8, 4, 15, 3, 20],3))