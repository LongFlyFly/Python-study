import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv('D:\\qq专属\\查询结果.csv', encoding='utf-8')
dataset.head()
dataset.shape
dataset.info()
#处理缺失数据
dataset.isnull().sum()  #判断缺失值
print(dataset.isnull().sum())
#处理异常值
dataset.describe()
print(dataset.describe())
print('去重前：',dataset.shape)
 #面积箱线图进行分析
df = pd.DataFrame(dataset['area'])
df.plot.box(title="Check outliers for house area")
plt.grid(linestyle="--", alpha=0.3)
plt.show()
 #总价箱线图进行分析
df = pd.DataFrame(dataset['price'])
df.plot.box(title="Check outliers for house area")
plt.grid(linestyle="--", alpha=0.3)
plt.show()
normal = dataset[dataset.price<=322.5]        #总价处理异常值
normal = dataset[dataset.area<=129.1725]      #面积处理异常值
#处理重复值
normal.drop_duplicates(keep='first',
                       subset='name',
                       inplace=True)      #通过卖点处理重复行
print('去重后：',normal.shape)
print(normal.info())
print('卖点不重复的信息:',normal['name'].unique())
len(normal['name'].unique())          #得到卖点不重复的信息数量
print('朝向不重复的信息:',normal['towards'].unique())
len(normal['towards'].unique())   #得到朝向不重复信息的数量
print('位置不重复的信息:',normal['location'].unique())
len(normal['location'].unique())  #得到位置不重复信息的数量
normal.drop(['towards','location'],axis=1,inplace=True)   #删除朝向和位置信息
print('装修情况:',normal['fitment'].unique())
len(normal['fitment'].unique())   #得到装修情况的数量
#价格去掉字符
print(dataset['unitprice'].map(lambda x: str(x).lstrip('元/㎡').rstrip('元/㎡')).astype(float).describe())
normal = pd.get_dummies(normal,columns=['fitment'], drop_first=True)  #将装修情况单独一列
print(normal.head())
print('矩阵的长度',normal.shape)
print('基本信息',normal)