from collections import deque

n, k = map(int, input().split())
l = list(map(int, input().split()))

pref = [0] * (n + 1)

for i in range(1, n + 1):
    pref[i] = pref[i - 1] + l[i - 1]

stk = deque([0])
maxi = float("-inf")
maxl = 0

for i in range(1, n + 1):
    while stk and i - stk[0] > k:
        stk.popleft()

    curr = pref[i] - pref[stk[0]]

    if curr > maxi or (curr == maxi and i-stk[0]>maxl):
        maxi = curr
        maxl = i - stk[0]

    while stk and pref[stk[-1]] > pref[i]:
        stk.pop()

    stk.append(i)

print(maxl)