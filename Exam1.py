def countwords(l):
    d={}
    for i in l:
        if i not in d:
            d[i]=l.count(i)
    return d

n=int(input())
l=[]
for i in range(n):
    w=input().split()
    l+=list(w) 
f=countwords(l)
print(len(set(f.keys())))
for j in f.values():
    print(j, end = " ")