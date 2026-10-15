import nltk

nltk.download("punkt_tab")

from nltk.tokenize import word_tokenize

text="hello this is dhamu"

t=word_tokenize(text)
print(t)