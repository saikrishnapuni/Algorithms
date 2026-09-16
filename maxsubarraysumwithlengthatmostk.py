from collections import deque
def solve(arr,k):
    n = len(arr)
    pref = [0 for i in range(n+1)]
    for i in range(1,n+1):
        pref[i] = pref[i-1]+arr[i-1]
    stk = deque([0])
    maxi = float("-inf")
    maxl = 0
    for i in range(1,n+1):
        while(stk and i-stk[0]>k):
            stk.popleft()
        curr = pref[i]-pref[stk[0]]
        if(curr>maxi or (curr == maxi and i-stk[0]>maxl)):
            maxi = curr
            maxl = i-stk[0]
        while(stk and pref[stk[-1]]>pref[i]):
            stk.pop()
        stk.append(i)
    return maxi,maxl
print(solve([2, -1, 3, 4, -2, 5],3))