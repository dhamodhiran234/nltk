import nltk

nltk.download("punkt_tab")
nltk.download("stopwords")
nltk.download("wordnet")

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer


text="i am dhamu , this is learning from nltk procession"

word=word_tokenize(text)
sw=stopwords.words("english")

new=[]
for i in word:
    if i not in sw:
        new.append(i)
print("tokenize:",word)
print("stop_wprds:",new)

ps=[]
for i in new:
    p=PorterStemmer()
    k=p.stem(i)
    ps.append(k)
print("stemming:",ps)

lm=[]
for i in word:
    l=WordNetLemmatizer()
    k=l.lemmatize(i,pos="v")
    lm.append(i)
print("lemmatizer:",lm)