class Fenwick:
    def __init__(self,n):
        self.n = n
        self.bit = [0 for i in range(self.n+1)]
    def update(self,i,val):
        while(i<=self.n):
            self.bit[i] += val
            i = i+(i&(-i))
    def query(self,i):
        ans = 0
        while(i>0):
            ans += self.bit[i]
            i = i-(i&(-i))
        return ans
arr  = [2,14,1,3,16,27]
n = len(arr)
s_arr = list(set(arr))
d = {}
for i in range(0,len(s_arr)):
    d[s_arr[i]] = i+1
ans = [0 for i in range(n)]
f = Fenwick(len(d))
for i in range(0,n):
    ans[i] = f.query(d[arr[i]]-1)
    f.update(d[arr[i]],1)
print(ans)