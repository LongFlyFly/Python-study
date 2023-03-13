#----------------数据处理----------
import pandas as pd
df = pd.read_csv(r'路径')
#查看数据信息
df.info()
#描述性的统计信息-----describe()
df.describe()
#排序
dfg=df.set_index('列名')

#axis = 1删除列，0删除行
df.drop([],axis = 1).groupby(['位置分组'])
df.sort_values(['按成交量排序'],)
#数据分组
a=df['成交量'].groupby(df["位置"])
a = a.mean()#求平均值
#求个数，size()
a=df['成交量'].groupby(df["位置"],df['卖家'])
a=a.size()
#数据分割
df1=df[30:40][['位置'],['卖家']]
#数据合并
#concat()合并行，maerge()合并列

#-------------pandas-----------------

import pandas as pd
#提供数据清洗，也用于挖掘和数据分析
#1、读数据
df = pd.read_csv(r'路径')
df.head()#默认取前五行，可查看数据

#2、保存数据         保存a,b两列          索引          表头
df.to_csv('路径名',columns=['a','b'],index=False ,headers =True)
#label可以自己定,索引默认是0,1,2...
#3、切片
rows = df[0:3]#取行
cols = df[['a','b']]#取多列要[],用列名取
rcols = df.loc[1:3['a','b']]#取行和列，取得1，2，3行，取得是标签（左闭右闭）
rcolss = df.iloc[1:3['a','b']]#取得是索引，取得2,3行（左闭右开）
#4、创建新的列-----销售量
df['销售量'] = df['价格']*df['成交量']
#5、数据过滤 map()函数过滤
df['及格'] = df['成绩'].map(lambda x:'通过' if x>60 else '挂科')
data = df[df['价格']<100&df['成交量']>10000]
#------------数据转换--------------


import csv
import json

data=[]
with open(r'F:\数据文件\house.csv','r',encoding='utf-8') as f:
    for row in csv.DictReader(f): #每次读一行,读字典
        data.append(row)
    json_data = json.dump(data)


#转换成csv
with open('JSON文件路径','r') as f:
    dicts = json.load(f)#把json转换成字典
out = open('','w')
writer = csv.DictWriter(out,dicts[0].keys())#写表头
writer.writeheader()
writer.writerows(dicts) #批量处理
out.close()

#从csv中读取数据
# pandas.read  


