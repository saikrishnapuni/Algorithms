from bisect import bisect_left
class Fenwick:
    def __init__(self,n):
        self.n = n
        self.bit = [0 for i in range(0,self.n+1)]
    def update(self,i,val):
        while(i<=self.n):
            self.bit[i]+=val
            i = i+(i&(-i))
    def query(self,i):
        ans = 0
        while(i>0):
            ans += self.bit[i]
            i = i - (i&(-i))
        return ans
a = [3,3,3]
b = [3,3,3]
n = len(a)
a_sor = list(set(a))
a_sor.sort()
d = {}
for i in range(len(a_sor)):
    d[a_sor[i]]=i+1
f = Fenwick(len(d))
c = 0
for i in range(0,n):
    idx = bisect_left(a_sor,b[i])
    c+=f.query(idx-1)
    f.update(d[a[i]],1)
print(c)
