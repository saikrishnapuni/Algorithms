from collections import deque

def solve(s, k, l):
    n = len(s)
    pref = [0 for i in range(n + 1)]

    for i in range(1, n + 1):
        pref[i] = -1 if s[i - 1] == '0' else 1
        pref[i] += pref[i - 1]

    stk = deque()

    for i in range(k, n + 1):

        while stk and stk[0] < i - l:
            stk.popleft()

        
        j = i - k
        while stk and pref[stk[-1]] > pref[j]:
            stk.pop()
        stk.append(j)

        
        if pref[i] - pref[stk[0]] > 0:
            return True

    return False