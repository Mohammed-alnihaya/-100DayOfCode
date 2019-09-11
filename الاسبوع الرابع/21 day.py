s_sets={1,3,5,6,'a','x','d'}
print(len(s_sets))
print(s_sets)
s_sets.remove(1)# حذف العنصر محدد
s_sets.discard('a')# حذف العنصر محدد
print(s_sets)
s=s_sets.pop()
print(s)
print(s_sets)

