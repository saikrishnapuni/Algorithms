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

def ReversePairs(arr,n):
    B = arr[::]
    B.sort()
    ans = 0
    Fen = Fenwick(B)
    for i in range(0,n):
        l=0
        h = n-1
        ind = -1
        while(l<=h):
            mid = (l+h)//2
            if(B[mid] == arr[i]):
                ind = mid
                break
            elif(B[mid]>arr[i]):
                h = mid-1
            else:
                l = mid+1
        ans = ans+Fen.prefixSum(ind)
        Fen.update(ind+1,1)
    return ans
arr = [3,5,1,7,2]
n = len(arr)
print(ReversePairs(arr,n))
                
        
    
        