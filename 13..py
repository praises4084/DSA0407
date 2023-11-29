import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

reviews = [
    "This product is amazing! I love it.",
    "The quality of this item is really good.",
    "Not satisfied with the product. It didn't meet my expectations."
]

all_reviews = ' '.join(reviews)

tokens = word_tokenize(all_reviews)

freq_dist = FreqDist(tokens)

print("Frequency distribution of words in customer reviews:")
for word, frequency in freq_dist.items():
    print(f"{word}: {frequency}")
