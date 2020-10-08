#!/usr/bin/python
#-*-coding:utf-8-*-

class Animals:
    # 构造函数，通过默认值初始化
    def __init__(self,name,age=20):
        self.name=name
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
    members = 0

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


class Document():
    #类的常量
    WELCOME_STR = 'Welcome! The context for this book is {}.'

    def __init__(self, title, author, context):
        print('init function called')
        self.title = title
        self.author = author
        self.__context = context

    # 类函数
    @classmethod
    def create_empty_book(cls, title, author):
        return cls(title=title, author=author, context='nothing')

    # 成员函数
    def get_context_length(self):
        return len(self.__context)

    # 静态函数
    @staticmethod
    def get_welcome(context):
        return Document.WELCOME_STR.format(context)


empty_book = Document.create_empty_book('What Every Man Thinks About Apart from Sex', 'Professor Sheridan Simove')
print(Document.WELCOME_STR)
print(empty_book.get_context_length())
print(empty_book.get_welcome('indeed nothing'))

#抽象类和抽象方法
from abc import ABCMeta, abstractmethod


class Entity(metaclass=ABCMeta):
    @abstractmethod
    def get_title(self):
        pass

    @abstractmethod
    def set_title(self, title):
        pass


class Document(Entity):
    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title


document = Document()
document.set_title('Harry Potter')
print(document.get_title())
#如下代码报错，抽象类无非实例化
#entity = Entity()


