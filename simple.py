import nltk

nltk.download("punkt_tab")
nltk.download("stopwords")
nltk.download("wordnet")

import re

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

text="hello this is dhamu speaking of @0297e238964732 studies"

text = re.sub(r"[^a-zA-Z\s]", "", text)


word=word_tokenize(text)

sm=stopwords.words("english")

new=[]
for i in word:
    if i not in sm:
        new.append(i)

stemmer=[]
for i in new:
    f=PorterStemmer()
    g=f.stem(i)
    stemmer.append(g)

lemmat=[]
for i in new:
    f=WordNetLemmatizer()
    g=f.lemmatize(i)
    lemmat.append(g)


print("tokenization:",word)
print("stop worda:",new)
print("stemmer:",stemmer)
print("lemmatization:",lemmat)


