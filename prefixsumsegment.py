class pSegment:
    def __init__(self,arr):
        self.arr = arr
        self.n = len(arr)
        k = 1
        while(k<self.n):
            k = k*2
        self.segment = [0 for i in range(2*k-1)]
        for i in range(0,self.n):
            self.segment[k-1+i] = self.arr[i]
        for i in range(k-2,-1,-1):
            self.segment[i] = self.segment[2*i+1]+self.segment[2*i+2]
        self.k = k
        print(self.segment)
    def update(self,ind,X):
        self.arr[ind] += X 
        p = 0
        ss = 0
        se = self.k-1
        while(ss<se):
            mid = (ss+se)//2
            self.segment[p]+=X
            if(ind<=mid):
                p = 2*p+1
                se = mid
            else:
                p = 2*p+2
                ss = mid+1
        self.segment[p]+=X
        print(self.segment)
    def prefixsum(self,ind):
        p = 0
        ss = 0
        se = self.k-1
        sumi = 0
        while(ss<se):
            mid = (ss+se)//2
            if(ind>mid):
                sumi+=self.segment[2*p+1]
                p = 2*p+2
                ss = mid+1
            else:
                p = 2*p+1
                se = mid
        sumi+=self.segment[p]
        return sumi
    def plr(self,l,r):
        if(l>=1):
            return self.prefixsum(r)-self.prefixsum(l-1)
        return self.prefixsum(r)
            
arr = [1,2,3,4]
s = pSegment(arr)

s.update(3,10)
print(s.arr)
print(s.plr(1,3))