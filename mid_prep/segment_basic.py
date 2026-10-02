class Segment:
    def __init__(self,arr):
        self.n = len(arr)
        self.arr = arr
        self.k=1
        while(self.k<self.n):
            self.k = self.k*2
        self.segement = [self.n for i in range(self.k)]
        for i in range(0,self.n):
            self.segement[i] = i
        self.segement = [0 for i in range(self.k-1)]+self.segement
        for i in range(self.k-2,-1,-1):
            
            a = self.segement[2*i+1]
            b = self.segement[2*i+2]
            if(a == self.n):
                self.segement[i] = b
            elif(b == self.n):
                self.segement[i] = a
            else:
                if(self.arr[a]>self.arr[b]):
                    self.segement[i] = b
                else:
                    self.segement[i] = a
            
            
    def update(self,i,val):
        self.arr[i] = val
        i = (self.k-1+i-1)//2
        while(i>=0):
            a = self.segement[2*i+1]
            b = self.segement[2*i+2]
            if(a == self.n):
                self.segement[i] = b
            elif(b == self.n):
                self.segement[i] = a
            else:
                if(self.arr[a]>self.arr[b]):
                    self.segement[i] = b
                else:
                    self.segement[i] = a
            i = (i-1)//2
    def query(self,l,r,ss,se,i):
        if(l<=ss and se<=r):
            return self.segement[i]
        elif(l>se or r<ss):
            return self.n
        else:
            mid = (ss+se)//2
            left = self.query(l,r,ss,mid,2*i+1)
            right = self.query(l,r,mid+1,se,2*i+2)
            if(left == self.n):
                return right
            elif(right == self.n):
                return left
            mini = min(self.arr[left],self.arr[right])
            if(mini == self.arr[left]):
                return left
            return right
        
arr = [2,5,3,4,6,1]
s = Segment(arr)

print(s.query(1,4,0,s.k-1,0))  

s.update(2,10)
print(s.segement)
print(s.query(1,4,0,s.k-1,0))  