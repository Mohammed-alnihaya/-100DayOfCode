f_sets={"A",'B','C','D'}
print(f_sets)
s={1,3,4,2,3}
print(s)
for x in s:
    print(x)

print("A" in f_sets)

s.add(6)
print(s)

s.update([8,7,9])#الحظ : أن العناصر ال ُمضافة يجب أن تكون داخل قوسين مربعين []
print(s)
