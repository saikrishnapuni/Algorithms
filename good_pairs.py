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
def reversePairs(A,B,n):
    Asorted = list(set(A))
    Asorted.sort()
    n1 = len(Asorted)
    ans = 0
    fen = Fenwick(Asorted)
    for i in range(0,n):
        
        l = 0
        h = n1-1
        ind1 = n1
        while(l<=h):
            mid = (l+h)//2
            if(Asorted[mid]<B[i]):
                l = mid+1
            else:
                ind1 = mid
                h = mid-1
        ans = ans+fen.prefixSum(ind1)
        l = 0
        h = n1-1
        ind = -1
        while(l<=h):
            mid = (l+h)//2
            if(Asorted[mid] == A[i]):
                ind = mid
                break
            elif(Asorted[mid] < A[i]):
                l = mid+1
            else:
                h = mid-1
        fen.update(ind+1,1)
    return ans
n=int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
print(reversePairs(a,b,n))