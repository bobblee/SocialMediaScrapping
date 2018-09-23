import re
import nltk
from nltk.corpus import stopwords
from textblob import TextBlob
import itertools as it

#Input Strings to test
StringHate  = "i hate pizza."
StrongHate  = "I HATE PIZZA."
StringLove  = "I love pizza."
StrongLove  = "I LOVE PIZZA."
InputString = "I hate pizza. I love pizza"
ComboString = StringHate+StringLove

List_String = [StringHate,StrongHate,StringLove,StrongLove,InputString,ComboString]

#Load stopwords
stop_words = stopwords.words('english')

#Semtiment Analysis value descriptions
print("The polarity score is a float within the range [-1.0, 1.0].")
print("The subjectivity is a float within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective.")

#Loop through
for TestString in List_String :
#Semtiment Analysis Input String tests
    Start_String    = TestString.lower()
    print(Start_String)

    CleanString     = re.sub(r"(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", Start_String)
    print(CleanString)

    Tokenize        = CleanString.split()
    print(Tokenize)

    NoStopList    = ' '.join([word for word in Tokenize if word not in stop_words])
    print(NoStopList)

    analysis      = TextBlob(NoStopList)
    print(analysis.sentiment)
