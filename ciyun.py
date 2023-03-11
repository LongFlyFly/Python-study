from wordcloud import WordCloud
import jieba
text = open(r'D:\python\hong.txt',"r", encoding='utf-8').read()
cut_text=jieba.lcut(text)
wc = WordCloud(
    font_path='D:python/font/simhei.ttf'
)
wc.generate(' '.join(cut_text))
wc.to_file('D:\python\红色文化效果图.png')

