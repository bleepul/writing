import spacy
from spacy import displacy

nlp = spacy.load('en_core_web_lg')
doc = nlp(u'There were several thousand head and they were moving quarterwise toward the company.')

for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
          token.shape_, token.is_alpha, token.is_stop)

for chunk in doc.noun_chunks:
    print(chunk.text, chunk.root.text, chunk.root.dep_,
          chunk.root.head.text)

displacy.serve(doc, style='dep')