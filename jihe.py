from wordcloud import WordCloud
text = open(r'D:\python\iii.txt',"r").read()
print(text)
wc = WordCloud()
wc.generate(text)
wc.to_file("D:\python\英文效果图.png")
