from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn import preprocessing
from sklearn import svm
from sklearn import model_selection
from sklearn.grid_search import GridSearchCV
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics import precision_score
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
import csv

train_data = pd.read_csv('train_set.csv', sep="\t")
train_data = train_data[0:1000]
print train_data.count()

le = preprocessing.LabelEncoder()
my_categories = le.fit_transform(train_data["Category"])
components_to_use = 40
svd = TruncatedSVD(n_components=components_to_use)
count_vectorizer = CountVectorizer(stop_words=ENGLISH_STOP_WORDS)
X = count_vectorizer.fit_transform(train_data["Content"])
X.toarray()
my_content = svd.fit_transform(X)
clf = svm.SVC(C=1000.0, kernel='rbf', gamma=1e-05)
clf.fit(my_content, my_categories)

#Let's bring the test file to test our accuracy
test_data = pd.read_csv("test_set.csv", sep="\t")
for_testing = count_vectorizer.transform(test_data["Content"])
for_testing.toarray()
omgomg = svd.transform(for_testing)
y_pred = clf.predict(omgomg)
predicted_categories = le.inverse_transform(y_pred)
print predicted_categories

mylist = [[]]
counter = 0
for rownum, row in test_data.iterrows():
    mylist.append([row['Id'],predicted_categories[counter]])
    counter = counter + 1
testSet = pd.DataFrame(mylist, columns=['Id', 'Category'])
testSet.to_csv('testSet_categories.csv', index=False, sep='\t')


