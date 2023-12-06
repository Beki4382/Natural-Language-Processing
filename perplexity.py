import math
import calculating_probability
probabilities_1 = calculating_probability.probabilities_1
probabilities_2 = calculating_probability.probabilities_2
probabilities_3 = calculating_probability.probabilities_3
probabilities_4 = calculating_probability.probabilities_4


def calculate_perplexity(test_set, ngram_probabilities):
    N = len(test_set)
    perplexities = []

    for n, ngram_probs in enumerate(ngram_probabilities, start=1):
        perplexity = 1

        for phrase in test_set:
            phrase = phrase.split(" ")
            ngram_size = min(n, len(phrase))

            for i in range(len(phrase) - ngram_size + 1):
                ngram = " ".join(phrase[i:i + ngram_size])
                ngram_probability = ngram_probs.get(ngram, 1e-10)  # Use a small value for unseen N-grams
                perplexity *= 1 / ngram_probability

        perplexity = pow(perplexity, 1/N)
        perplexities.append(perplexity)
        print(f"Perplexity for n={n}: {perplexity}")

    return perplexities

test_set = ["ኢትዮጵያ ታሪካዊ ሀገር ናት", "ሰላም እንደ ገና ሆኖ አነስተኛ እንደ ሆነ ነው"]
ngram_probabilities = [probabilities_1, probabilities_2, probabilities_3, probabilities_4]

perplexities = calculate_perplexity(test_set, ngram_probabilities)
