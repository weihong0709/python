import  sys
#捕获单个异常
try:
    s = input('please enter two numbers separated by comma: ')
    num1 = int(s.split(',')[0].strip())
    num2 = int(s.split(',')[1].strip())
    ...
except ValueError as err:
    print('Value Error: {}'.format(err))
#捕获多个异常
#写法一
try:
    s = input('please enter two numbers separated by comma: ')
    num1 = int(s.split(',')[0].strip())
    num2 = int(s.split(',')[1].strip())
    ...
except (ValueError, IndexError) as err:
    print('Error: {}'.format(err))

print('continue')

#写法二
try:
    s = input('please enter two numbers separated by comma: ')
    num1 = int(s.split(',')[0].strip())
    num2 = int(s.split(',')[1].strip())
    ...
except ValueError as err:
    print('Value Error: {}'.format(err))
except IndexError as err:
    print('Index Error: {}'.format(err))
#最后增加捕获所有异常,有两种写法
try:
    s = input('please enter two numbers separated by comma: ')
    num1 = int(s.split(',')[0].strip())
    num2 = int(s.split(',')[1].strip())
    ...
except ValueError as err:
    print('Value Error: {}'.format(err))
except IndexError as err:
    print('Index Error: {}'.format(err))
except Exception as err:
    print('Other error: {}'.format(err))

try:
    s = input('please enter two numbers separated by comma: ')
    num1 = int(s.split(',')[0].strip())
    num2 = int(s.split(',')[1].strip())
    ...
except ValueError as err:
    print('Value Error: {}'.format(err))
except IndexError as err:
    print('Index Error: {}'.format(err))
except:
    print('Other error')

print('continue')
#带finally的异常处理
try:
    f = open('file.txt', 'r')
    # some data processing
except OSError as err:
    print('OS error: {}'.format(err))
except:
    print('Unexpected error:', sys.exc_info()[0])
finally:
    try:
        f.close()
    except:
        print(sys.exc_info()[0])

#自定义异常
class MyInputError(Exception):
    """Exception raised when there're errors in input"""
    def __init__(self, value):  # 自定义异常类型的初始化
        self.value = value

    def __str__(self):  # 自定义异常类型的 string 表达形式
        return ("{} is invalid input".format(repr(self.value)))
#通过raise抛出异常
try:
    raise MyInputError(1)  # 抛出 MyInputError 这个异常
except MyInputError as err:
    print('error: {}'.format(err))

try:
    raise MyInputError(1)  # 抛出 MyInputError 这个异常
except MyInputError as err:
    raise err
