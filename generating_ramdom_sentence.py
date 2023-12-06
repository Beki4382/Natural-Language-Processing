import random
import calculating_probability

probabilities_1 = calculating_probability.probabilities_1
probabilities_2 = calculating_probability.probabilities_2
probabilities_3 = calculating_probability.probabilities_3
probabilities_4 = calculating_probability.probabilities_4


# Function to generate random sentences using N-grams
def generate_random_sentence(ngram_probs, n, length=10):
    sentence = []
    for _ in range(length):
        possible_ngrams = [ngram for ngram in ngram_probs.keys() if len(ngram) == n]
        chosen_ngram = random.choice(possible_ngrams)
        sentence.extend(chosen_ngram)
    return ' '.join(sentence)

# Assuming you have probabilities_1, probabilities_2, probabilities_3, probabilities_4
ngram_probabilities = [probabilities_1, probabilities_2, probabilities_3, probabilities_4]

# Generate random sentences for n-grams 1-4
for n, ngram_probs in enumerate(ngram_probabilities, start=1):
    random_sentence = generate_random_sentence(ngram_probs, n)
    print(f"Random Sentence for n={n}: {random_sentence}")
