import turtle
#str = input('请输入表白语：')
str = "给我的女孩~"
str1 = "2021-10-24"
turtle.speed(30)#画笔速度  数值越大，绘图越快！！！！！！
turtle.setup(1800,700,70,70)
turtle.color('black', 'pink')# 画笔颜色
turtle.pensize(3)   # 画笔粗细
turtle.hideturtle() # 隐藏画笔（先）
turtle.up() # 提笔
turtle.goto(-655, -255) # 移动画笔到指定起始坐标（窗口中心为0,0）
turtle.down()   #下笔
turtle.showturtle() #显示画笔
#画左边的小人
turtle.goto(-600,-200)
turtle.goto(-600,-120)
turtle.circle(35)
turtle.goto(-600,-200)
turtle.forward(40)
turtle.right(90)
turtle.forward(60)
turtle.hideturtle()
turtle.up()
turtle.goto(-600, -160)
turtle.down()
turtle.showturtle()
turtle.left(90)
turtle.forward(55)
turtle.right(45)
turtle.forward(20)
turtle.hideturtle()
turtle.up()
turtle.goto(-600, -145)
turtle.down()
turtle.showturtle()
turtle.goto(-545, -145)
turtle.left(90)
turtle.forward(20)

#画第一个爱心
turtle.color('pink', 'pink')
turtle.begin_fill()
turtle.hideturtle()
turtle.up()
turtle.goto(-500, -153)
turtle.down()
turtle.showturtle()
turtle.right(90)
turtle.forward(30)
turtle.left(90)
turtle.forward(30)
turtle.left(45)
turtle.circle(10.6,180)
turtle.left(180)
turtle.circle(10.6,180)
turtle.end_fill()
#下一个大爱心
turtle.color('pink', 'pink')
turtle.begin_fill()
turtle.hideturtle()
turtle.up()
turtle.goto(-430, -143)
turtle.down()
turtle.showturtle()
turtle.left(135)
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(45)
turtle.circle(17.67,180)
turtle.left(180)
turtle.circle(17.67,180)
turtle.end_fill()

#第三个爱心
turtle.color('pink', 'pink')
turtle.begin_fill()
turtle.hideturtle()
turtle.up()
turtle.goto(-315, -133)
turtle.down()
turtle.showturtle()
turtle.left(135)
turtle.right(90)
turtle.forward(70)
turtle.left(90)
turtle.forward(70)
turtle.left(45)
turtle.circle(24.74,180)
turtle.left(180)
turtle.circle(24.74,180)
turtle.end_fill()

#第四个爱心
turtle.color('pink', 'pink')
turtle.begin_fill()
turtle.hideturtle()
turtle.up()
turtle.goto(-187, -133)
turtle.down()
turtle.showturtle()
turtle.left(135)
turtle.right(90)
turtle.forward(70)
turtle.left(90)
turtle.forward(70)
turtle.left(45)
turtle.circle(24.74,180)
turtle.left(180)
turtle.circle(24.74,180)
turtle.end_fill()

#第5个爱心
turtle.color('pink', 'pink')
turtle.begin_fill()
turtle.hideturtle()
turtle.up()
turtle.goto(-43.7, -143)
turtle.down()
turtle.showturtle()
turtle.left(135)
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(45)
turtle.circle(17.67,180)
turtle.left(180)
turtle.circle(17.67,180)
turtle.end_fill()

#第6个爱心
turtle.color('pink', 'pink')
turtle.begin_fill()
turtle.hideturtle()
turtle.up()
turtle.goto(53.88, -153)
turtle.down()
turtle.showturtle()
turtle.right(90)
turtle.right(225)
turtle.forward(30)
turtle.left(90)
turtle.forward(30)
turtle.left(45)
turtle.circle(10.6,180)
turtle.left(180)
turtle.circle(10.6,180)
turtle.end_fill()

#画右边的小人
turtle.hideturtle()
turtle.up()
turtle.goto(251.28, -255)
turtle.down()
turtle.showturtle()
turtle.goto(196.28,-200)
turtle.goto(196.28,-120)
turtle.left(90)
turtle.circle(35)
turtle.goto(196.28,-200)
turtle.left(180)
turtle.forward(40)
turtle.left(90)
turtle.forward(60)
turtle.hideturtle()
turtle.up()
turtle.goto(196.28,-160)
turtle.down()
turtle.showturtle()
turtle.right(90)
turtle.forward(55)
turtle.left(45)
turtle.forward(20)
turtle.hideturtle()
turtle.up()
turtle.goto(196.28, -145)
turtle.down()
turtle.showturtle()
turtle.right(45)
turtle.forward(55)
turtle.right(45)
turtle.forward(20)

#画气球线和气球
#第一个气球
turtle.hideturtle()
turtle.up()
turtle.goto(-265, -133)
turtle.down()
turtle.showturtle()
turtle.goto(-245, 0)
turtle.right(135)
turtle.circle(35)
#第2个气球
turtle.hideturtle()
turtle.up()
turtle.goto(-265, -133)
turtle.down()
turtle.showturtle()
turtle.goto(-305, 80)
turtle.circle(40)

#补左一个气球
turtle.hideturtle()
turtle.up()
turtle.goto(-265, -133)
turtle.down()
turtle.showturtle()
turtle.goto(-350, 0)
turtle.circle(40)


#第3个气球
turtle.hideturtle()
turtle.up()
turtle.goto(-137, -133)
turtle.down()
turtle.showturtle()
turtle.goto(-167, 0)
turtle.circle(35)
#第4一个气球
turtle.hideturtle()
turtle.up()
turtle.goto(-137, -133)
turtle.down()
turtle.showturtle()
turtle.goto(-117, 80)
turtle.circle(40)
#右补一个气球
turtle.hideturtle()
turtle.up()
turtle.goto(-137, -133)
turtle.down()
turtle.showturtle()
turtle.goto(-70, 0)
turtle.circle(40)

#写字LOVE
turtle.pencolor("RED")
turtle.penup()
turtle.goto(-245,10)
turtle.write("幸",move=False,align='center',font=("微软雅黑",30,'normal'))

turtle.pencolor("ORANGE")
turtle.penup()
turtle.goto(-350,10)
turtle.write("很",move=False,align='center',font=("微软雅黑",30,'normal'))

turtle.pencolor("ORANGE")
turtle.penup()
turtle.goto(-305,90)
turtle.write("庆",move=False,align='center',font=("微软雅黑",30,'normal'))

turtle.pencolor("RED")
turtle.penup()
turtle.goto(-167,10)
turtle.write("遇",move=False,align='center',font=("微软雅黑",30,'normal'))

turtle.pencolor("ORANGE")
turtle.penup()
turtle.goto(-117, 90)
turtle.write("见",move=False,align='center',font=("微软雅黑",30,'normal'))

turtle.pencolor("ORANGE")
turtle.penup()
turtle.goto(-70, 10)
turtle.write("你",move=False,align='center',font=("微软雅黑",30,'normal'))

#写送给谁糖浆不分离
turtle.pencolor("pink")
turtle.penup()
turtle.goto(-220, 200)
turtle.write(str,move=False,align='center',font=("方正舒体",80,'normal'))

turtle.pencolor("RED")
turtle.penup()
turtle.goto(-210, -300)
turtle.write(str1,move=False,align='center',font=("方正舒体",50,'normal'))

window=turtle.Screen()
window.exitonclick()
