#with同等于java里面简化的try语句，不需要catch和finally，可以自动释放资源
with open('test.txt') as f:
    for line in f:
        print(line)
#自定义的类使用with语句
class WithTest:
    def method(self):
        print('method ok')
    def __enter__(self):
        print("enter with test")
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            print('exit success')
        else:
            print('exception')
            print(exc_tb)

with WithTest():
    print('begin withtest')
    raise NameError('test error')
