class Animals:
    # 构造函数，通过默认值初始化
    def __init__(self,name,age=20):
        self.name=name
        # 定义私有变量，体现封装
        # 定义私有变量，体现封装
        self.__age=age
    def fly(self):
        print('跑')
    def set_age(self,age):
        self.__age=age
    def get_age(self):
        return self.__age
    def set_name(self,  name):
        self.name=name
#创建对象
dog = Animals("狗",2)
print(dog.name)
print(dog.get_age())
dog.name='猫'
dog.age=3
print(dog.name)
print(dog.get_age())
dog.fly()
#室友变量无法直接访问
#print(dog.__age)
#继承,通过fly方法体现了多态
class Dog(Animals):
    def __init__(self,name):
        #调用父类的构造函数
        super().__init__(name)
    #方法覆盖
    def fly(self):
        print("我不能飞，只能跑")

dog = Dog('小狗')
print(dog.name)
print(dog.get_age())
dog.fly()

class Bird(Animals):
    def __init__(self,name,age):
        super().__init__(name,age)
    def fly(self):
        print("我能飞得很高")
littleBird=Bird('麻雀',5)
print(littleBird.name)
print(littleBird.get_age())
littleBird.fly()

class MemberCount:
    members=0
    def init(self):
        MemberCount.members+=1
m1 = MemberCount()
m1.init()
print(m1.members)
m2 = MemberCount()
m2.init()
print(m1.members)
print(m2.members)
m2.members=5
print(m1.members)
print(m2.members)

