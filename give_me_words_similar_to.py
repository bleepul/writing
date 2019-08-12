import spacy
import argparse

# initial arguments setup
parser = argparse.ArgumentParser()
parser.add_argument('-w', help='Word to lookup')
parser.add_argument('-n', help='Number of similar words to return')
args = parser.parse_args()


# https://spacy.io/ ... probably need to update this regularly
nlp = spacy.load('en_vectors_web_lg')


# the basic function
def most_similar(word, number):
    queries = [w for w in word.vocab if w.is_lower == word.is_lower]  # and w.prob >= -15]
    by_similarity = sorted(queries, key=lambda w: word.similarity(w), reverse=True)
    return [w.orth_ for w in by_similarity[:number]]


# print the output
count = 1
for w in most_similar(nlp.vocab[args.w], int(args.n)):
    print(w.lower())
    count = count + 1
    if count % 20 == 0:
        input()

# alternative form
# print([w.lower() for w in most_similar(nlp.vocab[args.w], int(args.n))])
