# Given a binary string of length \(n\), a substring is called dense if the number of 1s is greater than the number of 0s.

# Design an \(O(n\log n)\) time algorithm to compute the number of dense substrings.

def merge(arr,l,mid,h,ans):
    temp = []
    i = l
    j = mid+1
    while(i<=mid and j<=h):
        if(arr[i]<arr[j]):
            ans[0] = ans[0]+(h-j+1)
            temp.append(arr[i])
            i+=1
        else:
            temp.append(arr[j])
            j+=1
    while(i<=mid):
        temp.append(arr[i])
        i+=1
    while(j<=h):
        temp.append(arr[j])
        j+=1
    for i in range(0,h-l+1):
        arr[i+l]= temp[i]
def mergesort(arr, l, h, ans):
    if l >= h:
        return

    mid = (l + h) // 2

    mergesort(arr, l, mid, ans)
    mergesort(arr, mid + 1, h, ans)
    merge(arr, l, mid, h, ans)
def dense(s):
    n = len(s)
    pref = [0 for i in range(n+1)]
    for i in range(1,n+1):
        pref[i] = pref[i-1]
        if(s[i-1] == '0'):
            pref[i]-=1
        else:
            pref[i]+=1
    l = 0
    h = n
    ans = [0]
    mergesort(pref,l,h,ans)
    return ans[0]
print(dense("000111000111"))