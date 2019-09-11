sete={1,3,5,7,8}
sete.update([4,8,12]) # يجب وضع هذه [] لكي يتم الاضافة
print(sete)
print("------")
sete.remove(8)
print(sete)
print('------')
sete.clear()
print(sete)
print('------')

d={'name':'pigeon ','type':'bird',"skin cover":"feathers"}
print(d.get('type'))
print('-----')
d["skin cover"]='aaaa'
print(d)