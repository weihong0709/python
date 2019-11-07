#函数定义
def func_one(name):
    print(name)

func_one('liuweihong')
#文档字符串
def func_document():
    'this is func_document'
    print('ok')
print(func_document.__doc__)
#带单个返回值和多个返回值
def func_return_one():
    return 'one parameter'
print(func_return_one())

#带多个返回值，多个参数以元组的方式返回
def func_return_more():
    return 'test',11,True
print(func_return_more()[0])
print(func_return_more()[1])
print(func_return_more()[2])
#作用域，只有全局作用域和函数作用域,通过global在函数里面定义或者关联全局变量
global_var=123
def func_scope():
    global global_var
    global_var = 234
    global global_var2
    global_var2='function global_var2'
    print(globals())
    i=3
    if(i>2):
        internal_var = 'internal'
    print(internal_var)
    print(locals())
func_scope()
print(global_var)
print(global_var2)
#函数修改外部可变对象，会作用于外部对象，字符串（数字）、元组不可变对象不会对外部有影响
def func_args_scope(para):
    temp=list(para)
    temp.append(11)
    temp2=[1,2]
    print(temp2)
MIN_VALUE = 1
MAX_VALUE = 10
def validation_check(value):
    MIN_VALUE += 1
validation_check(5)

paraList = [1,2,3]
func_args_scope(paraList)
print(paraList)
#关键字参数，关键字参数可指定默认值
def func_keyword(name,age=32):
    print(name)
    print(age)
#位置参数必须放前面，不能跟在关键字参数后面，关键字参数放最后面
func_keyword('liuweihong',age=45)
#下面的非法
#func_keyword(name='liuweihong',45)
#收集参数-->使用单个星号收集非关键字可变参数，收集为元组
def func_args(first,*others):
    print(first)
    print(others)
func_args('one','two','three')
#收集参数-->使用2个星号收集关键字可变参数，收集为字典
def func_keyword_args(first,**others):
    print(first)
    print(others)

func_keyword_args('first',name='liuweihong',age=2)

#分配参数
#1、通过*号可以将


