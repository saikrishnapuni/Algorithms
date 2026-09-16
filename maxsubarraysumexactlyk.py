def solve(arr,k):
    maxi = float("-inf")
    n = len(arr)
    sumi = 0
    for i in range(0,k):
        sumi+=arr[i]
    maxi = max(maxi,sumi)
    for i in range(k,n):
        sumi-=arr[i-k]
        sumi+=arr[i]
        maxi = max(maxi,sumi)
    return maxi
print(solve([2, -1, 3, 4, -2, 5],3))