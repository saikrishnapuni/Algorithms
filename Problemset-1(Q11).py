# Given a stream of n (about 109) numbers, design an O(n) time and O(k) space
# algorithm to find an element of rank k
def quickselect(arr,l,h,k):
    if(l>h):
        return -1
    arr,i = partition(arr,l,h,k)
    r = i-l+1
    if(r == k):
        return arr[i]
    elif(r>k):
        return quickselect(arr,l,i-1,k)
    else:
        return quickselect(arr,i+1,h,k-r)
    
def partition( arr, low, high,k):
        # code here
    pivot = arr[low]
    i = low+1
    j = high
    while(i<=j):
        while(i<=j and arr[i]>=pivot):
            i+=1
        while(i<=j and arr[j]<=pivot):
            j-=1
        if(i<j):
            arr[i],arr[j] = arr[j],arr[i]
    arr[low],arr[j] = arr[j],arr[low]
    return arr,j
def findrank(arr,k):
    n = len(arr)
    l = 0
    h = n-1
    return quickselect(arr,l,h,k)
import heapq

def find_rank(stream, k):
    heap = []

    for x in stream:
        if len(heap) < k:
            heapq.heappush(heap, x)

        elif x > heap[0]:
            heapq.heapreplace(heap, x)

    return heap[0]

print(findrank([7, 2, 10, 4, 15, 6, 12, 3],3))