a={'A':'apple','B':'bob','C':'car','D':'22 day'}
print(a)

print('------------'
      )

print(a['C'])# للوصول للعناصر نستخدم المفتاح الخاص بالعنصر، ونضع هذا المفتاح داخل أقواس مربعة [].

print(a.get('D'))# get دالة حصل على العنصر
a['B']='model'
print(a)
print('________')
for z in a:#تستخدم الفور لعرض المفاتيح

    print(z)
print('----')
for x in a:
    print(a[x])# أما لعرض جميع القيم في القاموس نستخدم هذه الطريقة في الطباعة
print('-------')
for v in a.values():# كذلك هذه الدالة تطبع القيمة
    print(v)
print('-------')
for c in a.items():# ترجع القيمة مع المفتاح
    print(c)

