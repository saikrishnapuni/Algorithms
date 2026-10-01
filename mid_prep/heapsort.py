def bottomup(arr,n):
    while((n-1)//2 >=0 and arr[(n-1)//2]>arr[n]):
        arr[n],arr[(n-1)//2] = arr[(n-1)//2],arr[n]
        n = (n-1)//2
def topdown(arr,i,n):
    while(2*i+2<n and arr[i]>min(arr[2*i+1],arr[2*i+2])):
        if(arr[2*i+2]<arr[2*i+1]):
            arr[i],arr[2*i+2] = arr[2*i+2],arr[i]
            i = 2*i+2
        else:
            arr[i],arr[2*i+1] = arr[2*i+1],arr[i]
            i = 2*i+1
    while(2*i+1<n and arr[i]>arr[2*i+1]):
        arr[i],arr[2*i+1] = arr[2*i+1],arr[i]
        i = 2*i+1
      
def heapsort(arr,n):
    i = n//2 -1
    for i in range(n//2 -1 ,-1,-1):
        topdown(arr,i,n)
    while(n>0):
        arr[0],arr[n-1] = arr[n-1],arr[0]
        topdown(arr,0,n-1)
        n=n-1
    print(arr[::-1])
arr = [10,3,8,17,4,5,6]
heapsort(arr,len(arr))
    