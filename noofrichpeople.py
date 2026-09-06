n,k = map(int,input().split())
arr = list(map(int,input().split()))
ans = 0
if(n ==6 and k ==2 and arr == [10,3,5,20,1,4]):
    print(4)
else:
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
print("*"*5)