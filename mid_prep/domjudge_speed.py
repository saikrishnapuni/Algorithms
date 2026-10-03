import heapq as hp
n,k = map(int,input().split())
mod = 10**9 + 7
speed = []
eff = []
for _ in range(n):
    a,b = map(int,input().split())
    speed.append(a)
    eff.append(b)
heap = []
for i in range(0,n):
    hp.heappush(heap,[-speed[i],eff[i]])
print(heap)
sumi = 0
mini = float("inf")
while(k>0):
    a = hp.heappop(heap)
    sumi = (sumi -a[0])%mod
    mini = min(mini,a[1])
    k-=1
maxi = (sumi*mini)%mod
print(maxi,sumi,mini)
heap=[]

