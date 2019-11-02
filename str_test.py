#字符串定义
s1 = 'hello'
s2 = "hello"
s3 = """hello"""
s4='''hello'''
print(s1 == s2 == s3==s4)
#Python 的三引号字符串，则主要应用于多行字符串的情境，比如函数的注释等等
def calculate_similarity(item1, item2):
    """
    Calculate similarity between two items
    Args:
        item1: 1st item
        item2: 2nd item
    Returns:
      similarity score between item1 and item2
    """
print(calculate_similarity.__doc__)
myname='''
liu
weihong
'''
print(myname)
#字符串的常用操作
name='liuweihong'
#通过索引随机访问
print(name[0])
#切片操作
print(name[1:2])
print(name[:])
#in 和 not in操作
print('liu' in name)
print('liu' not in name)
#重复操作符*
print(name*2)
#连接操作符+
print(name+name)
#遍历字符串
for c in name:
    print(c)
#+=在python2.5后不一定创建新的字符串
str1='sss'
str2='dddd'
str1 += str2
print(str1)
#string.join(iterable)
l=['1','2','cc']
str3 = str1.join(l)
print(str3)
#split函数
path = 'hive://ads/training_table'
namespace = path.split('//')[1].split('/')[0] # 返回'ads'
print(namespace)
#strip去掉首尾指定的字符 lstrip rstrip 去掉左右的指定字符
strp=' aa bb '
print(strp.strip(" "))
print(strp.lstrip(" "))
print(strp.rstrip(" "))
#字符串格式化 新旧两种方式，推荐新的方式
id=101
name='liu weihong'
#新方式
print('no data available for person with id: {}, name: {}'.format(id, name))
#老方式
print('no data available for person with id: %d, name: %s' % (id, name))





