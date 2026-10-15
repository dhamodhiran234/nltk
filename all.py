# import nltk
# import string

# nltk.download("punkt_tab")
# nltk.download("stopwords")

# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
# from nltk.stem import WordNetLemmatizer
# from nltk import pos_tag

# text="My Name IS Dhamu,My password Has @123."


# #split data into word by words:

# word=word_tokenize(text)

# #data cleaning in :

# clean=[]
# for i in word:
#     if i not in string.punctuation :
#         f=i.lower()
#         clean.append(f)

# num_rem=[]
# for i in clean:
#     if not i.isdigit():
#         num_rem.append(i)


# print(num_rem)

# # remove stop words:

# # stop=stopwords.words("english")

# # stops=[]
# # for i in num_rem:
# #     if i not in stop:
# #         stops.append(i)

# # print(stops)

# # lemmations:;:

# # verb=[]
# # ad=[]
# # no=[]

# # for i in num_rem:
# #     l=WordNetLemmatizer()
# #     k=l.lemmatize(i,pos='v')
# #     verb.append(k)
# #     k=l.lemmatize(i,pos='a')
# #     ad.append(k)
# #     k=l.lemmatize(i,pos='n')
# #     no.append(k)

# # print(verb)
# # print(ad)
# # print(no)

# print(pos_tag(num_rem))

# for word,tag in pos_tag(num_rem):

#     if tag.startswith("V"):
#         pos='v'
#     elif tag.startswith("N"):
#         pos='n'
#     else :
#         pos='a'
#     t=WordNetLemmatizer()
#     f=t.lemmatize(word,pos=pos)
#     print(word,'=>',f)





# import nltk
# from nltk.tokenize import word_tokenize
# from collections import Counter

# nltk.download('punkt')

# # Sample documents (corpus)
# corpus = [
#     "AI and NLTK make text processing easy.",
#     "Text processing and tokenization are fun with AI."
# ]

# # Step 1: Tokenize and lowercase all documents
# tokenized_corpus = [word_tokenize(doc.lower()) for doc in corpus]

# # Step 2: Create a vocabulary (unique words across all documents)
# vocab = sorted(list(set(word for doc in tokenized_corpus for word in doc)))
# print("Vocabulary:", vocab)
# print("-" * 50)

# # Step 3: Create Bag-of-Words vectors (word counts) for each document
# bow_vectors = []
# for doc in tokenized_corpus:
#     print(doc)
#     # Count frequencies of words in the document
#     word_counts = Counter(doc)
#     print(word_counts)
    
#     # Create a vector matching the vocabulary order
#     vector = [word_counts[word] for word in vocab]
#     # print(vector)
#     bow_vectors.append(vector)

# # Print results
# # print(bow_vectors)
# for i, vec in enumerate(bow_vectors):
#     print(f"Document {i+1} BoW Vector: {vec}")