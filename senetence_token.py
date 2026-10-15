import nltk

nltk.download("punkt_tab")

from nltk.tokenize import sent_tokenize

text='''
this is dhamu,
this is ragul
'''

# t=sent_tokenize(text)


# print(t)

t=sent_tokenize(text)
for i in range(len(t)):
    print(t[i])