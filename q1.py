n =  int(input())
sumi = 0
while(n>0):
    rem = n%10
    sumi = sumi+rem
    n = n//10
print(sumi)