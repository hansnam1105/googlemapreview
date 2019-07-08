import numpy as np
import pandas as pd
import re
from bs4 import BeautifulSoup

df = pd.read_json("review.json", encoding='UTF-8')

def parser(body):
    bs = BeautifulSoup(body, 'html.parser')
    user_name = bs.find('span', jstcache = '215').text
    date = bs.find('span', jstcache='242').text
    ratingorg = bs.find('span', class_ = 'section-review-stars').text
    ratingtemp = str(bs).split('개 \" ')[0]
    ratingtemp = ratingtemp.split('별표 ')[1]
    review_text = bs.find('span', jstcache = '245').text
    return user_name, date, ratingtemp, review_text
    
df['user_name'], df['date'], df['rating'], df['review_text'] = zip(*df['body'].map(parser))
del df["body"]
df = df.applymap(lambda x: x.replace('\U0001f44d','').replace('\U0001f618',''))

df.to_csv('google.csv', encoding = 'cp949')

#Rating 그래프 분석
import seaborn as sns 
import matplotlib.pyplot as plt
sns.catplot('rating',kind='count',data=df)
plt.title('rating')
plt.show()
print(df['rating'].value_counts())
high_rate_review = df[df['rating'] == '5']['review_text']
low_rate_review = df[df['rating'] <= '2']['review_text']
high_rate_review = high_rate_review.apply(lambda x:re.sub('[^가-힣\s\d]',"",x))
low_rate_review = low_rate_review.apply(lambda x:re.sub('[^가-힣\s\d]',"",x))

#워드 클라우드 파이썬과 JVM의 버전차이로 현재 불가능
from konlpy.tag import Twitter
from collections import Counter
from wordcloud import WordCloud

low_tagger = Twitter()
high_tagger = Twitter()

def get_word_low_rating(sentence):
    nouns = low_tagger.nouns(sentence)
    return [noun for noun in nouns if len(noun) > 1]

def get_word_high_rating(sentence):
    nouns = high_tagger.nouns(sentence)
    return [noun for noun in nouns if len(noun) > 1]

low_rating_document = low_rate_review.values
high_rating_document = high_rate_review.values    

font_path = 'c:\\windows\\fonts\\NanumGothic.ttf'
wordcloud = WordCloud(
    font_path = font_path,
    width = 800,
    height = 800,
    background_color = "white"
    ).generate(np.array2string(high_rating_document))
plt.figure(figsize = (6,5), dpi =120)
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()
