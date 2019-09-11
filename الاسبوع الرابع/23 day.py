d={'name':'mohammed','age':21,'N':'ksa','car':'yes'}

if 'name' in d:
    print('ok')

print(len(d))
d['color']='black'
print(d)
d.pop('N')
print(d)
d.popitem()
print(d)
del d['age']
print(d)
d.clear()
print(d)
del d
