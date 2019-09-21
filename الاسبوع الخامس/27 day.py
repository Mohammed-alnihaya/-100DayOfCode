a=1
b=1
print("A") if a>b else print("B") if a==b else print("c")

v=int(input(" enter your gread: "))

if v<100 and v>=90:
        print("your gread is  A")

elif v <89 and v>=80:
        print("your gread is  B")

elif v<79 and v>=70:
        print("your gread is  C")

elif v<69 and v>=60:
        print("your gread is  D")

else: print("your gread is F")
