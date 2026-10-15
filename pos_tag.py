# import nltk
# import re

# nltk.download("punkt_tab")
# nltk.download("stopwords")
# nltk.download("wordnet")
# nltk.download("averaged_perceptron_tagger_eng")

# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
# from nltk import pos_tag
# from nltk.stem import PorterStemmer
# from nltk.stem import WordNetLemmatizer

# text="hello this is dhamu speacial if 00056"


# text=re.sub(r"[^a-zA-z\s]","",text)
# print(text)

# word=word_tokenize(text)
# sw=stopwords.words("english")

# new=[]
# for i in word:
#     if i not in sw:
#         new.append(i)

# stemm=[]
# for i in word:
#     g=PorterStemmer()
#     t=g.stem(i)
#     stemm.append(t)

# lemm=[]
# pos=[]
# for i in word:
#     g=WordNetLemmatizer()
#     t=g.lemmatize(i,pos='v')
#     lemm.append(t)


# for i in word:
#     if g.lemmatize(i,pos='v'):
#         print("it is verb")
#     elif g.lemmatize(i,pos='n'):
#         print("it is noun")

#     elif g.lemmatize(i,pos='a'):
#         print("it is adverb")
#     else:
#         print('not')

# t=pos_tag(word)
# print(t)

# print(new)
# print(stemm)
# print(lemm)



import nltk

nltk.download("punkt_tab")
nltk.download("averaged_perceptron_tagger_eng")
nltk.download("wordnet")

from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer

text="hello this is dhamu special movements"

word=word_tokenize(text)

pt=pos_tag(word)

for word,tag in pt:
    if tag.startswith("V"):
        pos='v'
    elif tag.startswith("N"):
        pos='n'
    else :
        pos='a'
    t=WordNetLemmatizer()
    f=t.lemmatize(word,pos=pos)
    print(word,'=>',f)
    

print(word)
print(pt)
