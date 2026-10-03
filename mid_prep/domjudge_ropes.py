import heapq as hp
n =  int(input())
l = list(map(int,input().split()))
hp.heapify(l)
c = 0
sumi = 0
while(len(l)>1):
    a = hp.heappop(l)
    b = hp.heappop(l)
    sumi+=(a+b)
    hp.heappush(l,a+b)
    
print(sumi)