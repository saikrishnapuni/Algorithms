def solve(arr):
    maxi = float("-inf")
    sumi = 0
    for i in arr:
        sumi = sumi+i
        maxi = max(maxi,sumi)
        if(sumi<0):
            sumi = 0
    return maxi
print(solve([-5, -2, -8, -1, -3]))