from math import sqrt
def getNum():
    nums = []
    iNumStr = input("请输入数字：")
    while iNumStr != "":
        nums.append(eval(iNumStr))
        iNumStr = input("请输入数字：")
    return nums
def mean(numbers):   #计算平均值
    s=0
    for num in numbers:
        s=s+num
    return s/len(numbers)
def dev(numbers,mean):    #计算标准差
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num-mean)**2
    return sqrt(sdev/(len(numbers)-1))
def median(numbers):
    new = sorted(numbers,reverse=True)
    print(new)
    size = len(numbers)
    if size%2==0:
        med = (new[size//2-1]+new[size//2])/2
    else:
        med = new[size//2]
    return med
def getMax(numbers):
    max=numbers[0]
    for num in range(0,len(numbers)):
        if max<numbers[num]:
            max=numbers[num]
    return (max)
def getMin(numbers):
    min=numbers[0]
    for num in range(0,len(numbers)):
        if min>numbers[num]:
            min=numbers[num]
    return (min)

n=getNum()
m=mean(n)
print("平均值:{},标准差:{:.2},中位数:{}.,最大值:{},最小值:{}".format(m,dev(n,m),median(n),getMax(n),getMin(n)))