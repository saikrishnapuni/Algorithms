class Fenwick:
    def __init__(self,arr):
        self.arr = arr
        self.n = len(arr)
        self.bit = [0 for i in range(0,self.n+1)]
        for i in range(1,self.n+1):
            j = i
            while(j<=self.n):
                self.bit[j] += self.arr[i-1]
                j = j+(j&-j)
            
                
                
        print(self.bit) 
    def update(self,i,X):
        while(i<=self.n):
            self.bit[i]+=X
            i = i+(i&-i)
    def prefixSum(self,i):
        sumi = 0
        while(i>0):
            sumi+=self.bit[i]
            i = i-(i&-i)
        return sumi
arr = [3,2,-1,-2,3,4,5,-1,0,-2,5,3,6,2,1,4]
fen = Fenwick(arr)
print(fen.prefixSum(2))