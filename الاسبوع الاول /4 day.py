z=1j            # حرف  j/J يرمز لرقم التخيلي ولا يستخدم اي حرف اخر لوصف هذا الرقم، ولايمكن تحويله الى اي نوع اخر
print(type(z))
v=-123345677
print(type(v))
e=34e4
print(type(e))

import random # طريق للاستدعاء

print(random.randrange(1,100))
print(random.randint(1,100))
from random import randint  #  طريق للاستدعاء بتحديد شي معين

print(randint(10,30))
u=randint(20,39)
print(" U= ",u)