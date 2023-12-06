import nltk
nltk.download('punkt')
from nltk import ngrams
from collections import Counter


# Function to generate N-grams
def generate_ngrams(text, n):
    return list(ngrams(text, n))

# Load the Amharic Corpus with a specified limit
corpus_path = "/content/GPAC.txt"
limit_characters = 5000000

ngrams_1 = []
ngrams_2 = []
ngrams_3 = []
ngrams_4 = []

with open(corpus_path, 'r', encoding='utf-8') as file:
    corpus_chunk = file.read(limit_characters)

# Tokenize the limited corpus
tokens = nltk.word_tokenize(corpus_chunk)

# Create N-grams for n=1, 2, 3, 4
ngrams_1.extend(generate_ngrams(tokens, 1))
ngrams_2.extend(generate_ngrams(tokens, 2))
ngrams_3.extend(generate_ngrams(tokens, 3))
ngrams_4.extend(generate_ngrams(tokens, 4))

# Sample prints for the limited dataset
print("-----------------Unigrams----------------")
for i in range(5):
  print(ngrams_1[i])

print("-----------------bigrams----------------")
for i in range(5):
  print(ngrams_2[i])

print("-----------------trigrams----------------")
for i in range(5):
  print(ngrams_3[i])

print("-----------------quadrigrams----------------")
for i in range(5):
  print(ngrams_4[i])