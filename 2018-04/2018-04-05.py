class Person:


    # 下面的用户、密码、邮箱为硬代码，写死了不能更改的，若需要修改看2018-04-06.py
    username = 'xiaoming'
    passwd = '123456'
    email = '123456@23.com'

    def register(self):
        print('user_register',self.username,self.passwd,self.email)

    def login(self):
        print('user_login',self.username,self.passwd)


p = Person()
p.register()
p.login()