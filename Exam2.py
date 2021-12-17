def bigger_is_greater(w):
    m=list(w)
    i=len(m)-1
    j=i
    while m[i-1] >= m[i] and i>0:
        i -= 1
    if i<1:
        return "no answer"
    while m[j]<=m[i-1]:
        j -= 1
    m[j],m[i-1]=m[i-1],m[j]
    return m
n=int(input())
l=[]
l2=[]
for i in range(n):
    w=input().split()
    l+=list(w)
for j in range(len(l)):
    print(bigger_is_greater(l[j]))