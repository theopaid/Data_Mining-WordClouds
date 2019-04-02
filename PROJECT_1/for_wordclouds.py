from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn import preprocessing
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
from os import path
import matplotlib.pyplot as plt

train_data = pd.read_csv('train_set.csv', sep="\t")
for rownum, row in train_data.iterrows():
    if(row["Category"] == 'Business'):
        f = open("BusinessContent.txt", "a+")
        f.write(row["Content"] + " ")
    if(row["Category"] == 'Politics'):
        f = open("PoliticsContent.txt", "a+")
        f.write(row["Content"] + " ")
    if(row["Category"] == 'Film'):
        f = open("FilmContent.txt", "a+")
        f.write(row["Content"] + " ")
    if(row["Category"] == 'Football'):
        f = open("FootballContent.txt", "a+")
        f.write(row["Content"] + " ")
    if(row["Category"] == 'Technology'):
        f = open("TechnologyContent.txt", "a+")
        f.write(row["Content"] + " ")

d = path.dirname(__file__)

# Read the whole text.
text = open(path.join(d, 'FilmContent.txt')).read()
stopwords = set(STOPWORDS)
# Save the generated image:
wordcloud = WordCloud(max_font_size=40, stopwords=stopwords).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.savefig("Films.png")

text = open(path.join(d, 'BusinessContent.txt')).read()
# Save the generated image:
wordcloud = WordCloud(max_font_size=40, stopwords=stopwords).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.savefig("Business.png")

text = open(path.join(d, 'FootballContent.txt')).read()
# Save the generated image:
wordcloud = WordCloud(max_font_size=40, stopwords=stopwords).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.savefig("Football.png")

text = open(path.join(d, 'TechnologyContent.txt')).read()
# Save the generated image:
wordcloud = WordCloud(max_font_size=40, stopwords=stopwords).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.savefig("Technology.png")

text = open(path.join(d, 'PoliticsContent.txt')).read()
# Save the generated image:
wordcloud = WordCloud(max_font_size=40, stopwords=stopwords).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.savefig("Politics.png")
