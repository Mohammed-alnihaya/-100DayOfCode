def q (n):
    return lambda a:a*n

h=q(3)
a=q(7)
print(h(11))
print(a(11))
