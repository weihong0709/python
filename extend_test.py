class Animal:
    def fly(self):
        print("animal fly")
class Person:
    def fly(self):
        print('python fly')
    def sleep(self):
        print('person quick')
class Cat(Person,Animal):
    pass
cat = Cat()
cat.fly();
cat.sleep()
