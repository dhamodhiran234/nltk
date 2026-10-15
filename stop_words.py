import nltk

nltk.download("punkt_tab")
nltk.download("stopwords")

from nltk.tokenize import word_tokenize

from nltk.corpus import stopwords

t="i am learning in python tutorials"

text=word_tokenize(t)

# print(text)

st=stopwords.words("english")

print(st)

print(len(st))

new=[]
stop=[]
for i in text:
    if i not in st:
        new.append(i)
    else:
        stop.append(i)
print(" no stop_words:",new)
print("stop_words:",stop)

