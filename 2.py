import random
class Human(object):
    def __init__(self,name,weight):
        self.name=name
        self.weight=weight

    def run(self):
        print("{}正在跑步".format(self.name))

    def eat(self):
        print("{}正在吃饭".format(self.name))

class Man(Human):
    def __init__(self,name,weight=random.randint(60,90)):
        self.name=name
        self.weight=weight

    def run(self):
        self.weight-=0.3

    def eat(self):
        self.weight+=0.2

    def yundong(self):
        for i in range(1,31):
            self.run()
            for x in range(1,4):
                self.eat()

        print("{}的体重{:.2f}".format(self.name,self.weight))

class Woman(Human):
    def __init__(self,name,weight=random.randint(40,60)):
        self.name=name
        self.weight=weight

    def run(self):
        self.weight-=0.2

    def eat(self):
        self.weight+=0.1

    def yundong(self):
        for i in range(1,31):
            self.run()
            self.run()
            self.eat()
            self.eat()
        print("{}的体重{:.2f}".format(self.name, self.weight))

mn=Man('猛男')
sn=Woman('淑女')
print(mn.name,mn.weight)
print(sn.name,sn.weight)
mn.yundong()
sn.yundong()