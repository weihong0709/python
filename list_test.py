#list遍历
l = [1, 2, 3, 4, 5, 6, 7]

for index in range(0, len(l)):#根据索引遍历
    if index < 5:
        print(l[index])

for index, item in enumerate(l):#使用enumerate方法得到索引和值
    if index < 5:
        print(item)
tupleA= (3,2,3,4)
print(tupleA)