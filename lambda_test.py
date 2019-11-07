functionA = lambda  x,y:x*y
print(functionA(2,3))

listA = [(lambda x: x*x)(x) for x in range(10)]
print(listA)

l = [(1, 20), (3, 0), (9, 10), (2, -1)]
l.sort(key=lambda x: x[1]) # 按列表中元祖的第二个元素排序
print(l)