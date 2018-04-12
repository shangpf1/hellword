
class Animal(object):
    
    def run(self):
        print('running......')

class Dog(Animal):

    def speak(self):
        print('speak......')


class Cat(Animal):
    def sleep(self):
        print('cat.....')

d = Dog()
d.run()
d.speak()

c = Cat()
c.run()
c.sleep()


class Person(object):

    user = 'lishsis'

    def __init__(self,username,passwd):
        self.username = username
        self.passwd = passwd
    
    @property     #属性
    def userinfo(self):
        print(self.username,self.passwd)

    @staticmethod   # 静态
    def unifo():
        print(Person.user)

p = Person('shangpf','spf2344')
p.userinfo
 

Person.unifo()