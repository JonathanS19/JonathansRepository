import pandas as pd

messages = pd.read_csv('C:/Users/LENOVO/OneDrive/College/Project/Data Science/NLP/spam finder/sms+spam+collection/SMSSpamCollection',sep='\t',names=['label','message'])

import re 
import nltk

from nltk.corpus import stopwords 
from nltk.stem import WordNetLemmatizer
lemma = WordNetLemmatizer()
corpus = []

for i in range(0,len(messages)):
    review = re.sub('[^a-zA-Z]',' ',messages['message'][i]) 
    review = review.lower()
    review = review.split()
    
    review = [lemma.lemmatize(word) for word in review if word not in (stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)
    
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 3000)
x =cv.fit_transform(corpus).toarray()
    
y = pd.get_dummies(messages['label'])
y = y.iloc[:,1].values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)

from sklearn.naive_bayes import MultinomialNB
spam_detec = MultinomialNB().fit(x_train,y_train)

y_pred = spam_detec.predict(x_test)

from sklearn.metrics import confusion_matrix
confusion = confusion_matrix(y_test,y_pred)

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test,y_pred)
print(accuracy)