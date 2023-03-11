# def aaa(x):
#     if not isinstance(x>0, (int, float)):
#         raise TypeError('类型错误')
#     result=1
#     for i in range(1,x+1):
#         result=result*i
#     return result
# print(aaa(-1))

# def say_hi(year,age):
#     print('你好，你出身于{}年，你今年{}岁'.format(year,age))
# say_hi(2001,20)


# class Student():
#     pass
# zs=Student()
# zs.name='张三'
# print(zs.name)
# ls=Student()
# ls.name='李四'
# print(ls.name)
# print(zs,ls)

# class Student(object):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def info(self):
#         print("我的名字是{},今年{}岁".format(self.name,self.age))
# zs = Student('张三',19)
# zs.info()


class Student(object):
    def __init__(self,name='张三',age=19):
        if not isinstance(name,str):
            raise TypeError('name类型错误')
        if not isinstance(age,int) or age<0:
            raise TypeError('age类型错误')
        self.__name=name
        self.__age=age
    def info(self):
        print("我的名字是{},今年{}岁".format(self.__name,self.__age))

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age
zs = Student()
zs.info()

