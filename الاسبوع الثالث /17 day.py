i_tuple=('ali',2019,"copa",'A+')
z=input("enter what are you need ? ")
if z in i_tuple:
    print("here <--''-->")
else:
    print("sorry not here <-^^->")
print("_______")
s_tuple=("Mohammed",)*4
print(s_tuple)

x=(3,4,5,6)
x=x+(1,2,2,2,3)
print(x)

print("-----")

print(len(i_tuple)+len(s_tuple)+len(x))
print("--------")
thislist=[3,4,5,6,'A','B']
thistuple= tuple(thislist)
print(thistuple)
print('------')
print(x.count(2))
print(i_tuple.count("a"))
print(s_tuple.count("Mohammed"))