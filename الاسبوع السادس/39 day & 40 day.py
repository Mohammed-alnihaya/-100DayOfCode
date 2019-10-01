def power(n,p):
    if p:
        r=n*power(n,p-1)
    else:
        r=1
    return r

print(power(5,3))

l=[-4,-6,-5,-1,2,3,7,9,88]
v=[]
d=lambda a:a>0

for a in l:
    if (d(a)):
        v.append(a)


print(v)

