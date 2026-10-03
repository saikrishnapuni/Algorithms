import bisect
class Fenwick:
    def __init__(self,n):
        self.n = n
        
        self.bit1 = [0 for i in range(n+1)]
    def update(self,i,val):
        while(i<=self.n):
            
            self.bit1[i]+=1
            i+=(i&(-i))
    def query(self,i):
        ans = 0
        
        while(i>0):
            
            ans+=self.bit1[i]
            i = (i-(i&(-i)))
        return ans
        
n,k = map(int,input().split())
l = list(map(int,input().split()))
s_l = list(set(l))
s_l.sort()
d = {}
for i in range(0,len(s_l)):
    d[s_l[i]] =i+1

mini = -1
lo = 0
h=max(l)-min(l)
while(lo<=h):
    fen = Fenwick(len(d))
    ans = 0
    mid = (lo+h)//2
    
    for i in range(n-1,-1,-1):
        left = bisect.bisect_left(s_l, l[i]-mid)
        right = bisect.bisect_left(s_l, l[i])
        ans += fen.query(right) - fen.query(left)
        fen.update(d[l[i]],1)
    if(ans>=k):
        mini = mid
        h= mid-1
    else:
        lo = mid+1
print(mini)