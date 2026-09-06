a,b,c,d,r = map(int,input().split())

l = 1
h = max(b,d)

def find_rank(x):
    L = max(a,x)
    if L > b:
        c2 = 0
    else:
        c2 = b//2 - (L-1)//2

    L = max(c,x)
    if L > d:
        c3 = 0
    else:
        c3 = d//3 - (L-1)//3

    L = max(a,c,x)

    if L > min(b,d):
        c6 = 0
    else:
        c6 = min(b,d)//6 - (L-1)//6

    return c2+c3-c6


if find_rank(1) < r:
    print(-1)
else:
    while l <= h:
        mid = (l+h)//2

        r1 = find_rank(mid)

        if r1 >= r:
            l = mid+1
        else:
            h = mid-1

    print(h)