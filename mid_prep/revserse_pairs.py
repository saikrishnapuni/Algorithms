import bisect
class Segement:
    def __init__(self,n):
        self.n = n
        self.k = 1
        while(self.k<n):
            self.k*=2
        self.segment = [0 for i in range(2*self.k -1)]
    def update(self,i,val):
        idx = self.k-1+i
        self.segment[idx] +=val
        idx = (idx-1)//2
        while(idx>-1):
            self.segment[idx] = self.segment[2*idx+1]+self.segment[2*idx+2]
            idx = (idx-1)//2
    def query(self,i,ss,se,l,r):
        if(l<=ss and se<=r):
            return self.segment[i]
        elif(l>se or r<ss):
            return 0
        else:
            mid = (ss+se)//2
            left = self.query(2*i+1,ss,mid,l,r)
            right =  self.query(2*i+2,mid+1,se,l,r)       
            return left+right
arr = [6, 4, 1, 2, 7]
n = len(arr)
s_arr = list(set(arr))
s_arr.sort()
d = {}
for i in range(0,len(s_arr)):
    d[s_arr[i]] = i
s = Segement(len(d))
c = 0
for i in range(n-1,-1,-1):
    idx  = bisect.bisect_left(s_arr,arr[i]/2)
    c+=s.query(0,0,s.k-1,0,idx-1)
    s.update(d[arr[i]],1)
print(c)