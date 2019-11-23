from functools import reduce
#map函数,python3返回的是map对象需要转化为list
squared = map(lambda x: x**2, [1, 2, 3, 4, 5])
print(list(squared))
#zip函数

#filter函数
l = [1, 2, 3, 4, 5]
new_list = filter(lambda x: x % 2 == 0, l)
print(list(new_list))
#reduce函数
l = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, l)
print(product)

d = {'mike': 10, 'lucy': 2, 'ben': 30}

print(sorted(d.items(),key=lambda x:x[0]))

