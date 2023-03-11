import turtle as tk
from turtle import *
from random import random,randint

tk.setup(800,600)
tk.screensize(800,600,'black')
tk.speed(1)

for i in range(200):
    tk.speed(0)
    tk.pendown()
    tk.color('white')
    j = randint(-600,300)
    k = randint(-600,300)
    tk.pensize(2)
    tk.circle(1)
    tk.fillcolor('white')
    tk.penup()
    tk.goto(j,k)


tk.speed(1)
tk.color('lightblue')
tk.penup()
tk.goto(-350,210)
tk.pendown()
tk.write('To:老姐  ',font = ('方正舒体',32))

tk.penup()
tk.goto(-290,150)
tk.pendown()
tk.write('祝老姐越来越美丽',font = ('方正舒体',35))

tk.color('red')
tk.penup()
tk.goto(-270,-20)
tk.pendown()
tk.write(' 生  日  快  乐！',font = ('方正舒体',50))

tk.color('red')
tk.penup()
tk.goto(-280,-80)
tk.pendown()
tk.write('不止生日,每天都要开心呀！',font = ('方正舒体',30))

tk.color('lightblue')
tk.penup()
tk.goto(50,-200)
tk.pendown()
tk.write('来自你那头发极少的老弟',font=("方正舒体",12))

tk.color('lightblue')
tk.penup()
tk.goto(50,-220)
tk.pendown()
tk.write('龙清鑫 2021.10.01.',font=('方正舒体',12))

tk.done()
