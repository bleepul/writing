import spacy

nlp = spacy.load('en_vectors_web_lg')


def most_similar(word):
    queries = [w for w in word.vocab if w.is_lower == word.is_lower]  # and w.prob >= -15]
    by_similarity = sorted(queries, key=lambda w: word.similarity(w), reverse=True)
    return [w.orth_ for w in by_similarity[:200]]


#print(most_similar(nlp.vocab[u'black']))
print([w.lower() for w in most_similar(nlp.vocab[u'turrets'])])


# for foo in nlp.vocab:
#     if foo.orth_:
#         print(foo.orth_)
#print(dir(nlp.vocab[100].lex_id))
#print(nlp.vocab[100].lex_id)


# from spacy.matcher import Matcher
#
# patterns = {'HelloWorld': [{'LOWER': 'hello'}, {'LOWER': 'world'}]}
# matcher = Matcher(nlp.vocab)
# print(dir(matcher.vocab.strings))