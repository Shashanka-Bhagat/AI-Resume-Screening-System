import string

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Sample resume text
resume = """
Alice is an AI Engineer. She loves Machine Learning and Python!
"""

#lowercasing
resume=resume.lower()
print(resume)
print("-" * 50)

#removing punctuations
resume=resume.translate(str.maketrans(" "," ",string.punctuation))
print(resume)
print("-" * 50)

#tokenize
tokens=word_tokenize(resume)
print(tokens)
print("-" * 50)

#remove stopwords
stop_words=set(stopwords.words("english"))
tokens=[words for words in tokens if words not in stop_words]
print(tokens)
print("-" * 50)

#lemmatize
lemmatizer = WordNetLemmatizer()
tokens= [lemmatizer.lemmatize(words) for words in tokens]
print("final output")
print(tokens)