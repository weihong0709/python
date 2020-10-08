#!/usr/bin/python
#-*-coding:utf-8-*-
import functools
#简单装饰器
def my_decorator(func):
    def wrapper():
        print('wrapper of decorator')
        func()

    return wrapper


def greet():
    print('hello world')


greet = my_decorator(greet)
greet()

#装饰器的优雅表示
def my_decorator(func):
    def wrapper():
        print('wrapper of decorator')
        func()

    return wrapper


@my_decorator
def greet():
    print('hello world')


greet()


#带有参数的装饰器
def my_decorator(func):
    def wrapper(message):
        print('wrapper of decorator')
        func(message)

    return wrapper


@my_decorator
def greet(message):
    print(message)


greet('hello world')


#带有自定义参数的装饰器

def repeat(num):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num):
                print('wrapper of decorator')
                func(*args, **kwargs)

        return wrapper

    return my_decorator


@repeat(4)
def greet(message):
    print(message)


greet('hello world')

#装饰器会导致原函数元信息发送改变，通过functools方式可以解决
def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('wrapper of decorator')
        func(*args, **kwargs)

    return wrapper


@my_decorator
def greet(message):
    print(message)


print(greet.__name__)
#类装饰器
class Count:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print('num of calls is: {}'.format(self.num_calls))
        return self.func(*args, **kwargs)


@Count
def example():
    print("hello world")


example()
example()

#装饰器嵌套
import functools


def my_decorator1(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('execute decorator1')
        func(*args, **kwargs)

    return wrapper


def my_decorator2(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('execute decorator2')
        func(*args, **kwargs)

    return wrapper


@my_decorator1
@my_decorator2
def greet(message):
    print(message)


greet('hello world')

