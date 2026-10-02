import bisect
class Segment:
    def __init__(self,n):
        self.n = n
        self.k=1
        while(self.k<self.n):
            self.k = self.k*2
        self.segement = [0 for i in range(self.k)]
        
        self.segement = [0 for i in range(self.k-1)]+self.segement
    def update(self,i,val):
        self.segement[self.k-1+i]+=val
        idx = (self.k-1+i-1)//2
        while(idx>-1):
            self.segement[idx] = self.segement[2*idx+1]+self.segement[2*idx+2]
            idx = (idx-1)//2
    def query(self,l,r,ss,se,i):
        if(l<=ss and se<=r):
            return self.segement[i]
        elif(l>se or r<ss):
            return 0
        else:
            mid = (ss+se)//2
            left = self.query(l,r,ss,mid,2*i+1)
            right = self.query(l,r,mid+1,se,2*i+2)
            return left+right
n = 3
a = [3,3,3]
b = [3,3,3]
s = Segment(n)
a_sor = list(set(a))
a_sor.sort()
d = {}
for i in range(0,len(a_sor)):
    d[a_sor[i]] = i
c = 0
for i in range(0,n):
    idx = bisect.bisect_left(a_sor,b[i])
    c = c+s.query(0,idx-1,0,s.k-1,0)
    s.update(d[a[i]],1)
print(c)
     
            