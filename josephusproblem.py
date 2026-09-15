n, k = map(int, input().split())

ans = 0

for i in range(2, n + 1):
    ans = (ans + k) % i

print(ans)