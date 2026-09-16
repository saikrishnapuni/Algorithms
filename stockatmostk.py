from collections import deque
def solve(arr,k):
    maxi = float("-inf")
    stk = deque([0])
    for i in range(1,len(arr)):
        
        maxi = max(maxi,arr[i]-arr[stk[0]])
        while(stk and i-stk[0]>k):
            stk.popleft()
        while(stk and arr[stk[-1]]>=arr[i]):
            stk.pop()
        
        stk.append(i)
    return maxi
print(solve([10,2,8,4,15,3,20],3))