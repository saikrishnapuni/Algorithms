import math
class SegmentTree:
    def __init__(self,arr):
        self.n = len(arr)
        self.arr = arr
        self.segment = []
        for i in range(0,self.n):
            self.segment.append(i)
        if(self.n == 1):
            pow2 = 0
        else:
            pow2 = int(math.ceil(math.log2(self.n)))
        
        self.size = 2**pow2
        for j in range(0,(2**pow2)-self.n):
            self.segment.append(self.n)
        self.n2= len(self.segment)
        self.segment = self.segment[::-1]
        for j in range(1,(2**pow2)):
            self.segment.append(0)
        self.n1 = len(self.segment)
        self.segment = self.segment[::-1]
        for i in range(self.n1-self.n2-1,-1,-1):
            left = 2*i+1
            right = 2*i+2
            if(self.segment[left] == self.n):
                self.segment[i] = self.segment[right]
            elif(self.segment[right] == self.n):
                self.segment[i] = self.segment[left]
            else:
                if(arr[self.segment[left]]<arr[self.segment[right]]):
                    self.segment[i] = self.segment[left]
                else:
                    self.segment[i] = self.segment[right]
        print(self.segment)
    def update(self,ind,val):
        self.arr[ind] = val
        c = self.n1-self.n2+ind
        
        while(c>-1):
            a = (c-1)//2
            left = 2*a + 1
            right = 2*a + 2
            if(self.segment[left] == self.n):
                self.segment[a] = self.segment[right]
            elif(self.segment[right] == self.n):
                self.segment[a] = self.segment[left]
            elif(self.arr[self.segment[left]]>=self.arr[self.segment[right]]):
                self.segment[a] = self.segment[right]
            else:
                self.segment[a] = self.segment[left]
            c = a
            if(c == 0):
                c = -1
        print(self.segment,self.arr)
    def mlr(self,l,r,i,ss,se):
        if l <= ss and se <= r:
            return self.segment[i]

        elif l > se or r < ss:
            return self.n

        else:
            mid = (ss+se)//2

            left = self.mlr(l,r,2*i+1,ss,mid)
            right = self.mlr(l,r,2*i+2,mid+1,se)

            if left == self.n:
                return right
            elif right == self.n:
                return left
            elif self.arr[left] < self.arr[right]:
                return left
            else:
                return right
    def firstsmallerelement(self,X,p,ss,se):
        if(self.arr[self.segment[0]]>=X):
            return self.n
        while(ss<se):
            mid = (ss+se)//2
            if(self.arr[self.segment[2*p+1]]<X):
                se = mid
                p = 2*p+1
            else:
                p = 2*p+2
                ss = mid+1
        return self.segment[p]
    def lastsmallerelement(self,X,p,ss,se):
        if(self.arr[self.segment[0]]>=X):
            return -1
        while(ss<se):
            mid = (ss+se)//2
            if(self.arr[self.segment[2*p+2]]<X):
                p = 2*p+2
                ss = mid+1
            else:
                p = 2*p+1
                se = mid
        return self.segment[p]
    def nextSmaller(self,p,i,ss,se):
        ans = -1
        l = -1
        r = -1
        while(ss<se):
            mid = (ss+se)//2
            if(i<=mid):
                if(self.arr[self.segment[2*p+2]]<self.arr[i]):
                    ans = 2*p+2
                    
                    l = mid+1
                    r = se
                    
                p = 2*p+1
                se = mid
            else:
                
                p  = 2*p+2
                
                ss = mid+1
        if(ans == -1):
            return self.n
        return self.firstsmallerelement(self.arr[i],ans,l,r)
    def prevsmaller(self,p,i,ss,se):
        ans = -1
        l = -1
        r = -1

        while(ss < se):
            mid = (ss + se) // 2

            if(i <= mid):
            
                p = 2*p + 1
                se = mid

            else:
                
                if(self.arr[self.segment[2*p+1]] < self.arr[i]):
                    ans = 2*p + 1
                    l = ss
                    r = mid

                p = 2*p + 2
                ss = mid + 1

        if(ans == -1):
           return -1

        return self.lastsmallerelement(self.arr[i], ans, l, r)
arr = [7,5,4,8,2]
n = len(arr)
s = SegmentTree(arr)

idx = s.mlr(0, 2, 0, 0, s.size-1)

print(idx)
print(arr[idx])
ind = s.firstsmallerelement(1,0,0,n-1)
print(ind)
ind = s.firstsmallerelement(6,0,0,n-1)
print(ind)     