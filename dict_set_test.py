#集合的创建
d1 = {'name': 'jason', 'age': 20, 'gender': 'male'}
d2 = dict({'name': 'jason', 'age': 20, 'gender': 'male'})
d3 = dict([('name', 'jason'), ('age', 20), ('gender', 'male')])
d4 = dict(name='jason', age=20, gender='male')
print(d1 == d2 == d3 ==d4)
#集合的创建
s1 = {1, 2, 3}
s2 = set([1, 2, 3])
print(s1 == s2)
#字典访问元素
print(d1['name'])
print(d1.get('name'))
#判断元素在不在集合或者字典里面
if 'name' in d1:
    print(True)

if 1 in s1:
    print(True)
#字典的常用操作
#增加元素
d1['high']=10
print(d1)
#更新元素的值
d1['name']='liuweihong'
print(d1)
#删除元素
d1.pop('high')
print(d1)
#集合的常用操作
s1.add('4')
print(s1)
s1.remove('4')
print(s1)
#字典排序,对key和value进行排序，key和value类型需要一致
d_sorted_by_key = sorted(d1.items(), key=lambda x: x[0]) # 根据字典键的升序排序
print(d_sorted_by_key)
d5={'a':4,'b':2,'c':3}
d_sorted_by_value = sorted(d5.items(), key=lambda x: x[1]) # 根据字典值的升序排序
print(d_sorted_by_value)
#字典的遍历
d = {'name': 'jason', 'dob': '2000-01-01', 'gender': 'male'}
for k in d:  # 遍历字典的键
    print(k)

for v in d.values():  # 遍历字典的值
    print(v)

for k, v in d.items():  # 遍历字典的键值对
    print('key: {}, value: {}'.format(k, v))
