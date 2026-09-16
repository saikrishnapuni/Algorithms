def solve(arr):
    maxi = float("-inf")
    mini = arr[0]
    n = len(arr)
    for i in range(1,n):
        maxi = max(maxi,arr[i]-mini)
        if(mini>arr[i]):
            mini  =  arr[i]
    return maxi
print(solve([7,6,5,4,3,2,1]))