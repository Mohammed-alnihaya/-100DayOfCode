z=[1,'s','£',"ali","s"]
print(z)
print('------------')
z.append("Mohammed")
print(z)
print('------------')
s=z.copy()
print(s)
print('------------')
print(z.count("s"))
print('------------')
s.insert(3,'HHHHH')
print(s)
print('------------')
z.pop()
print('------------')


t_tuple=('java','python','swift')
if 'python' in t_tuple:
    print("here <___^^___> ")
else:
    print("not here <---''--->")