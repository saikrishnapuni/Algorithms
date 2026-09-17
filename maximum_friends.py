def solve(arr,x):
    arr.sort()
    maxi = 0
    n = len(arr)
    def bs(arr,val):
        l=0
        h =n-1
        ans = n
        while(l<=h):
            mid = (l+h)//2
            if(arr[mid]<val):
                
                l=mid+1
            else:
                ans = mid
                h = mid-1
        return ans
    for i in range(0,n):
        left = bs(arr,arr[i]-x+1)
        right = bs(arr,arr[i]+x)
        maxi = max(maxi,right-left-1)
    return maxi

print(solve ([1, 2, 3, 4, 5], 3))