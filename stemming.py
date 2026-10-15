import nltk

nltk.download("punkt_tab")
nltk.download("stopwords")


from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

text="i am learning in python with nltk"

word=word_tokenize(text)

stop_words=stopwords.words("english")

print(len(stop_words))

print(word)

new=[]
for i in word:
    if i not in stop_words:
        new.append(i)
print("processing_words:",new)

g=[]
for i in new:
    st=PorterStemmer()
    print(st)
    f=st.stem(i)
    g.append(f)

print("stemming:",g)
