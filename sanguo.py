import jieba
from wordcloud import WordCloud
#读取数据
text=open(r'D:/python/threekingdoms.txt',"r",encoding='utf-8').read()
cut_text=jieba.lcut(text)
wc= WordCloud(background_color='white',
                     font_path='D:python/font/simhei.ttf',
                     width=800, height=600)
index1 = {'曹操': ['孟德', '丞相','操曰'],
          '玄德': ['刘备', '刘皇叔', '皇叔', '玄德曰'],
          '云长': ['关羽', '关云长', '关公'],
          '孔明': ['诸葛亮', '诸葛曰', '诸葛', '孔明曰'],
          '张飞': ['翼德'],
          '赵云': ['子龙', '赵子龙'],
          '周瑜': ['公瑾', '都督']}
for t in index1.items():
    print(t)
    for x in t[1:]:
        for z in x:
            print(z)
            words = cut_text.count(z)
            idx = 0
            while words > 0:
                i = cut_text.index(z, idx, -1)
                cut_text[i] = t[0]
                idx = i + 1
                words -= 1

wc.generate(' '.join(cut_text))
wc.to_file('D:\python\三国2.png')