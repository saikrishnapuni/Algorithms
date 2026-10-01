def heapify(arr,n):
    while((n-1)//2>=0 and arr[n]<arr[(n-1)//2]):
        arr[n],arr[(n-1)//2] = arr[(n-1)//2],arr[n]
        n = (n-1)//2
        
def topdown(arr,n,i):
    while(2*i+2<n and arr[i]>min(arr[2*i+1],arr[2*i+2])):
        if(arr[2*i+1]<arr[2*i+2]):
            arr[i],arr[2*i+1] = arr[2*i+1],arr[i]
            i = 2*i+1
        else:
            arr[i],arr[2*i+2] = arr[2*i+2],arr[i]
            i = i*2 + 2
    while(2*i+1<n and arr[i]>arr[2*i+1]):
        arr[i],arr[2*i+1] = arr[2*i+1],arr[i]
        i = 2*i+1
        

arr = [10,3,8,17,4,5,6]
heap = []
c= 0
for i in range(len(arr)):
    heap.append(arr[i])
    c+=1
    heapify(heap,c-1)
print(heap)
n = len(arr)
for i in range(n//2-1,-1,-1):
    topdown(arr,n,i)
print(arr)
    