class Fenwick:
    def __init__(self,A):
        self.A = A
        self.n = len(self.A)
        self.bit = [0 for i in range(self.n+1)]
    def prefixSum(self,i):
        sumi = 0
        while(i>0):
            sumi = sumi+self.bit[i]
            i = i-(i&(-i))
        return sumi
    def update(self,i,x):
        while(i<=self.n):
            self.bit[i] += x
            i = i+(i &(-i))
            
def reversePairs(arr,n):
    left = [0 for i in range(n)]
    right = [0 for i in range(n)]
    b = list(set(arr))
    seen = 0
    b.sort()
    Fen = Fenwick(b)
    n1 = len(b)
    ans = 0
    for i in range(0,n):
        l = 0
        h = n1-1
        ind = -1
        while(l<=h):
            mid = (l+h)//2
            if(b[mid] == arr[i]):
                ind = mid
                h = mid-1
            elif(b[mid]>arr[i]):
                h = mid-1
            else:
                l = mid+1
        left[i] = Fen.prefixSum(ind)
        
        
        Fen.update(ind+1,1)
    Fen = Fenwick(b)
    for i in range(n-1,-1,-1):
        l = 0
        h = n1-1
        ind = -1
        while(l<=h):
            mid = (l+h)//2
            if(b[mid] == arr[i]):
                ind = mid
                h = mid-1
            elif(b[mid]>arr[i]):
                h = mid-1
            else:
                l = mid+1
        right[i] = seen-Fen.prefixSum(ind)
        Fen.update(ind+1,1)
        seen+=1
    for i in range(0,n):
        for j in range(i+1,n):
            ans = ans+(left[i]*right[j])
    return ans
print(reversePairs([3,22,77,4,5],5))