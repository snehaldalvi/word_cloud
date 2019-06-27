from wordcloud import WordCloud,STOPWORDS

comment=''
stopwords=set(STOPWORDS)
f=open("file.txt",'r+')
data=f.read().replace("\n",'')

wordcloud=WordCloud(width=500,height=600,background_color='blue',stopwords=stopwords,
	min_font_size=10).generate(data)

wordcloud.to_file('image.jpeg')
print("image saved successfully")




