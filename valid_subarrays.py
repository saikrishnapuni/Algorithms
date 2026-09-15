n = int(input())
l = list(map(int, input().split()))

nxt = [n] * n
stk = []

for i in range(n - 1, -1, -1):

    while stk and l[stk[-1]] >= l[i]:
        stk.pop()

    if stk:
        nxt[i] = stk[-1]

    stk.append(i)

ans = 0

for i in range(n):
    ans += nxt[i] - i

print(ans)