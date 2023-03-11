def calc_bmi(height,weight ):
    bmi = weight/pow(height,2)
    a=""
    if bmi<18.5:
        a="轻体重"
    elif bmi>=18.5 and bmi<24:
        a="健康体重"
    elif bmi>=24 and bmi<28:
        a="超重"
    elif bmi>=18.5:
        a="肥胖"
    print("您的BMI值为：{:.2f},您的体型为‘{}'".format(bmi,a))
height = eval(input('请输入你的身高:'))
weight = eval(input("请输入你的体重:"))
calc_bmi(height,weight)
