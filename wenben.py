# f='111.txt'
# with open('111.txt',encoding='utf-8') as f:
#     while  True:
#         text=f.read(6)
#         print(text,end='')
#         if text=='':
#            break
# f.close()

# f='111.txt'
# with open(f,'r',encoding='utf-8') as f:
#     for line in f:
#         print(line)


# f='111.txt'
# with open(f,'r',encoding='utf-8') as f:
#     txt=f.readlines()
# print(type(txt))
# print(txt)


# import os
# def getfiles(path):
#     files = []
#     for file in os.listdir(path):
#         name=os.path.join(path,file)
#         if os.path.isdir(name):
#             getfiles(name)
#         else :
#             files=name
#             print(files)
#     return files
# print(getfiles(r'D:\python'))

list2 = []
listMax = []
listMin = []
t = []
t1 = []
with open("111.txt", 'r', encoding="utf-8") as f:
    t = f.readlines()
    t1.append(t[0][0:14])
    for i in range(1,len(t)):
        t1.append(t[i][0:17])
    print(t)
    for i in range(1,len(t)):
        z1 = 9
        sum1 = 0
        zt = 9
        for zq in range(0, 3):
            sum1 += int(str(t[i])[zt:zt + 2])
            zt += 3
        print(sum1)
        list2.append(sum1)
    for z in range(0, 3):
        list1 = []
        for i in range(1, len(t)):
            x = str(t[i])[z1:z1 + 2]
            list1.append(x)
        print(list1)
        max = int(0)
        min = int(list1[0])
        for i in range(0, len(list1)):
            if max < int(list1[i]):
                max = int(list1[i])
        for i in range(0, len(list1)):
            if min > int(list1[i]):
                min = int(list1[i])
        listMax.append(max)
        listMin.append(min)
        print(max,min)
        z1 += 3
    with open("1111.txt", "a+", encoding="utf-8") as f1:
        f1.writelines(t1[0]+"，总分"+ "\n")
        t2 = 0
        for i1 in range(1,len(t)):
            f1.writelines(t1[i1] + "," + str(list2[t2])+ "\n" )
            t2 += 1
        f1.writelines("最高")
        for i in range(0, len(listMax)):
             f1.writelines("," + str(listMax[i]))
        f1.writelines("\n")
        f1.writelines("最低")
        for i in range(0, len(listMin)):
            f1.writelines("," + str(listMin[i]))
f.close()
print(list2)
print(listMax)
print(listMin)