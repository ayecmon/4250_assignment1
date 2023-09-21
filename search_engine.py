#-------------------------------------------------------------------------
# AUTHOR: Aye Mon
# FILENAME: search_engine.py
# SPECIFICATION: Calculation of how informative of a word in a document using tf-idf
# FOR: CS 4250- Assignment #1
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard arrays

#importing some Python libraries
import csv
import math
from collections import Counter

documents = []
labels = []

#reading the data in a csv file
with open('collection.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
         if i > 0:  # skipping the header
            documents.append (row[0])
            labels.append(row[1])

#Conduct stopWords Removal
tokenized_word = []
stopWords = {'I', 'and', 'She', 'They', 'her', 'their'}
for document in documents:
    words = document.split()
    for word in words:
        if word not in stopWords:
            tokenized_word.append(word)

#conduct stemming
stemmed_words = []
stemming = {
  "cats": "cat",
  "dogs": "dog",
  "loves": "love",
}
for word in tokenized_word:
    stemmed_words.append(stemming.get(word, word))
    tokenized_word = stemmed_words

#Identify the index terms.
terms = []
for word in tokenized_word:
    if word not in terms:
        terms.append(word)   

#tokenized documents
tokenized_documents = []
for document in documents:
    words = document.split()
    tokens = [stemming.get(word, word) for word in words if word not in stopWords]
    tokenized_document = [term for term in tokens if term in terms]
    tokenized_documents.append(tokenized_document)

# output tokenized documents
for i, tokenized_doc in enumerate(tokenized_documents):
    print(f"Tokenized Document {i + 1}:")
    print(tokenized_doc)
    print()

#term frequency function
def tf(document):
    term_frequency = Counter(document)
    num_terms = len(document)
    tf = {term: freq / num_terms for term, freq in term_frequency.items()}
    return tf
tf_calculation = [tf(doc) for doc in tokenized_documents]
print(tf_calculation )

#Inverse Document Frequency function
def idf(document, term):
    document_frequnecy = sum(1 for doc in document if term in doc)
    if document_frequnecy == 0:
        return 0
    idf = math.log10(len(document) / document_frequnecy)
    return idf

#calculation of idf
idf_values = {term: idf(tokenized_documents, term) for term in tokenized_doc}
print(idf_values)

docMatrix = []
for doc_tf in tf_calculation:
    tfidf_vector = [doc_tf.get(term, 0) * idf_values[term] for term in tokenized_doc]
    docMatrix.append(tfidf_vector)
print(docMatrix)

for i, row in enumerate(docMatrix):
    print(f"Tokenized Document {i + 1}:")
    for term, tfidf in zip(tokenized_doc, row):
        print(f"{term}: {tfidf:.4f}")
    print()

query = ["cat", "dog"]
#Binary query 
binary_query = {}
for term in set(query):
    if term in query:
        binary_query[term] = 1
    else:
        binary_query[term] = 0
print(binary_query)










