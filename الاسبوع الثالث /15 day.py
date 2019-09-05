e=["cut",'cup','cub']
print(len(e))#عدد العناصر
print(e)
e.append("cote")# اضافة في اخر القائمة
print(e)
e.insert(2,"cuz")# اضافة في مكان محدد
print(e)
e.remove("cuz")#حذف شئ محدد
print(e)
e.append("cute")
print(e)
e.pop()# حذف اخر شى في القائمة
print(e)
#e.clear()# حذف القائمة كاملة
print(e)
#q=e ليس طريقة صحيحة في نسخ بسبب اي تغير في المستقبل القائمة الاول يتم تغير القائمة الثانية تلقائي
print("_________")
z=e.copy() #هذه الطريق الصحيح في النسخ بسبب ان اي تغير في القائمة الاول لايؤثر على القائمة الثانية
print(z)
e.append("test")
print(e)
print(z)
r=list(e) #طريقة اخر لنسخ
print(r)
s=list(("a",'b','c','g','a`'))
print(s)
print(s.count("a")) #يظهر عدد العنصر المختار بحديد في القائمة
print(s.index("g"))# # يظهر عدد العناصر من البداية الى لبعنص المختار
print(s.sort())#؟؟؟؟؟