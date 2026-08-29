# Given three sorted arrays \(A\), \(B\), , design an efficient algorithm to find the \(k\)-th largest element among all elements in the 2  arrays.

# Convention: Rank 1 is the largest element.
def find_rank(A,B,la,lb,ha,hb,k,n,m):
    if(k == 0):
        mini = float("inf")
        if(ha<n-1):
            mini = min(mini,A[ha+1])
        if(hb<m-1):
            mini = min(mini,B[hb+1])
        return mini
    if(la<=ha and lb<=hb):
        mida = (la+ha)//2
        midb = (lb+hb)//2
        if(k<=(ha-la+hb-lb+2)//2):
            if(A[mida]<B[midb]):
                return find_rank(A,B,mida+1,lb,ha,hb,k,n,m)
            else:
                return find_rank(A,B,la,midb+1,ha,hb,k,n,m)
        else:
            if(A[mida]<B[midb]):
                return find_rank(A,B,la,lb,ha,midb-1,k-(hb-midb+1),n,m)
            else:
                return find_rank(A,B,la,lb,mida-1,hb,k-(ha-mida+1),n,m)
    else:
        if(la<=ha):
            return find_rank(A,B,la,lb,ha-k,hb,0,n,m)
        if(lb<=hb):
            return find_rank(A,B,la,lb,ha,hb-k,0,n,m)
            
            
def solve(A,B,k):
    n = len(A)
    m = len(B)
    la = 0
    lb = 0
    ha = n-1
    hb = m-1
    a = find_rank(A,B,la,lb,ha,hb,k,n,m)
    return a
   
    
A = [1, 5, 9]
B = [2, 6, 10]
k =4
print(solve(A,B,k)) 
