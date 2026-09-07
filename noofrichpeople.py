n,k = map(int,input().split())
arr = list(map(int,input().split()))
ans = 0
arr.sort()


for i in arr:
    target = k*i
    l = 0
    h = n-1
    c = n
    while(l<=h):
        mid = (l+h)//2
        if(arr[mid]>target):
            c = mid
            h = mid-1
        else:
            l = mid+1
   
    if(n-c<=k):
    
        ans+=1  
print(ans)
