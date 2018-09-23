#import nltk
#nltk.download('stopwords')


from nltk.corpus import stopwords
stopWords = set(stopwords.words('english'))
print(len(stopWords))
print(stopWords)