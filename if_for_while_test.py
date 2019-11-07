#条件与循环的复用
x=[1,2,3,-4,-5]
y = [value * 2 + 5 if value > 0 else -value * 2 + 5 for value in x]
print(y)

y = [value * 2 + 5  for value in x if value>0]
print(y)

x=[1,2,3]
y=[4,5,6]

result = [(xx, yy) for xx in x for yy in y if xx != yy]
print(result)
#
attributes = ['name', 'dob', 'gender']
values = [['jason', '2000-01-01', 'male'],
['mike', '1999-01-01', 'male'],
['nancy', '2001-02-01', 'female']
]
result=[]
for value in values:
    valueDict = {};
    for key,onevalue in zip(attributes,value):
        valueDict[key] = onevalue
    result.append(valueDict)
print(result)
result = [dict(zip(attributes,value))for value in values]
print(result)





