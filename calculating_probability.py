# Calculate probabilities of N-grams
from collections import Counter
import reading_corpus
ngrams_1 = reading_corpus.ngrams_1
ngrams_2 = reading_corpus.ngrams_2
ngrams_3 = reading_corpus.ngrams_3
ngrams_4 = reading_corpus.ngrams_4

def calculate_probabilities(ngrams_list):
    total_ngrams = len(ngrams_list)
    ngrams_counts = Counter(ngrams_list)
    probabilities = {ngram: count / total_ngrams for ngram, count in ngrams_counts.items()}
    return probabilities

# Calculate probabilities for each N-gram list
probabilities_1 = calculate_probabilities(ngrams_1)
probabilities_2 = calculate_probabilities(ngrams_2)
probabilities_3 = calculate_probabilities(ngrams_3)
probabilities_4 = calculate_probabilities(ngrams_4)

# Find the top 10 most likely N-grams
top_10_1 = dict(sorted(probabilities_1.items(), key=lambda x: x[1], reverse=True)[:10])
top_10_2 = dict(sorted(probabilities_2.items(), key=lambda x: x[1], reverse=True)[:10])
top_10_3 = dict(sorted(probabilities_3.items(), key=lambda x: x[1], reverse=True)[:10])
top_10_4 = dict(sorted(probabilities_4.items(), key=lambda x: x[1], reverse=True)[:10])

print("--------------Top 10 N-grams for unigrams------------------")
for key, val in top_10_1.items():
  print(key, ":", val)

print("--------------Top 10 N-grams for bigrams--------------------")
for key, val in top_10_2.items():
  print(key, ":", val)

print("-------------Top 10 N-grams for trigrams--------------------")
for key, val in top_10_3.items():
  print(key, ":", val)

print("-------------Top 10 N-grams quadrigrams----------------------")
for key, val in top_10_4.items():
  print(key, ":", val)
