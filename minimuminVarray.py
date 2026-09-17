def solve(arr):
    n = len(arr)
    l=1
    h=n-2
    if(n == 1):
        return arr[0]
    if(arr[0]<arr[1]):
        return arr[0]
    if(arr[n-2]>arr[n-1]):
        return arr[n-1]
    while(l<=h):
        mid = (l+h)//2
        if(arr[mid]<arr[mid-1] and arr[mid]<arr[mid+1]):
            return arr[mid]
        elif(arr[mid]<arr[mid+1] and arr[mid-1]<arr[mid]):
            h=mid-1
        else:
            l = mid+1
arr = [10, 8, 6, 2, 3, 4, 5, 7, 9]
print(solve(arr))