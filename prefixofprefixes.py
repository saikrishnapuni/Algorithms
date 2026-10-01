arr = [1,2,3,4,5]
n = len(arr)
pref = [0 for i in range(len(arr))]
pref_pref = [0 for i in range(len(arr))]
for i in range(0,n):
    pref[i] = pref[i-1]+arr[i]
pref_pref[0] = pref[0]
for i in range(1,n):
    pref_pref[i] = pref_pref[i-1]+pref[i]
print(pref)
print(pref_pref)