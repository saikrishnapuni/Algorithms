class Fenwick:
    def __init__(self,n):
        self.n = n
        self.bit = [0 for i in range(self.n+1)]
    def update(self,i,val):
        while(i<=self.n):
            self.bit[i]+=val
            i = i+(i&(-i))
    def query(self,i):
        ans = 0
        while(i>0):
            ans+=self.bit[i]
            i = i-(i&(-i))
        return ans
arr = [-10, -5, 6, 11, 15, 17]
n = len(arr)

s_arr = list(set(arr))
s_arr.sort()
d = {}
for i in range(0,len(s_arr)):
    d[s_arr[i]] = i+1
c = 0
fen =Fenwick(len(d))
for i in range(n-1,-1,-1):
    c+=fen.query(d[arr[i]]-1)
    fen.update(d[arr[i]],1)
print(c)
