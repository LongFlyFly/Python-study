import pandas as pd

dataset = pd.read_csv('D:\\下载的软件\\数据清洗01_身份信息_数据缺失清洗.csv', encoding='utf-8')
print(dataset.shape)
print(dataset.isnull().sum())
dataset1 = dataset.dropna()
print(dataset1)
delect_columns_list = list(set(list(dataset.columns)).difference(set(['性别','年龄'])))#处理性别和年龄中缺失的数据
dataset.dropna(subset=delect_columns_list, inplace=True)
dataset['创建日期'] = pd.to_datetime(dataset['创建日期'])#更改日期
print(dataset['创建日期'])
print(dataset.head())
print(dataset.shape)
def DBC2SBC(ustring_list):
    # '全角转半角'
    normal_str_list=[]
    for i in range(len(ustring_list)):
        rstring = ""
        for uchar in ustring_list[i]:
            inside_code = ord(uchar)
            if inside_code == 0x3000:
                inside_code = 0x0020
            else:
                inside_code -= 0xfee0
                if not (0x0021 <= inside_code and inside_code <= 0x7e):
                    rstring += uchar
                    continue
                rstring += chr(inside_code)
        normal_str_list.append(rstring)
    return normal_str_list
print(len(DBC2SBC(dataset['联系方式'])))
print(DBC2SBC(dataset['联系方式']))