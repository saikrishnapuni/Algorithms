def solve(arr,k):
    maxi = float("-inf")
    for i in range(0,len(arr)-k):
        maxi = max(maxi,arr[i+k]-arr[i])
    return maxi