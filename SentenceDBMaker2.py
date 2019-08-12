import spacy
import bookparser
from neo4j import GraphDatabase
import argparse, sys

uri = "bolt://localhost:7687"
d = GraphDatabase.driver(uri, auth=("neo4j", "password"))
tx = d.session()


parser = argparse.ArgumentParser()
parser.add_argument('--author', help='Do the bar option')
parser.add_argument('--work', help='Foo the program')
args = parser.parse_args()

auth = bookparser.Author
book = bookparser.WrittenWork

#auth.add(tx, args.author)
book.add(tx,  args.author, args.work,)

a = text = args.author.replace(' ', '')
b = text = args.work.replace(' ', '')
path = "Books/" + a + "/" + b


nlp = spacy.load('en_core_web_sm')
file = open(path, 'r')

book = file.read()
doc = nlp(book)


bp = bookparser.SentenceLoader()
for sent in doc.sents:
    sentence = []
    sentence_structure = []
    sentence_structure_detailed = []
    text = sent.text.rstrip()
    #bp.add_sentence(tx, text, args.work)

    for token in sent:
        if token.tag_ == '' or token.tag_ == "_SP":
            next
        else:
            t = bookparser.Token(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)
            t.add(tx)
            sentence.append(token.text)
            sentence_structure.append(token.pos_)
            sentence_structure_detailed.append(token.tag_)
            #print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)

    print(sentence)
    print(sentence_structure)
    print(sentence_structure_detailed)


print(args.author)
print(args.work)

#
# # import bracy
# #
# nlp = spacy.load('en_core_web_sm')
#
# author = ""
# work = ""
#
# #file = open('Books/HGWells/HGWELLS_IoDM', 'r')
# file = open('Books/CormacMcCarthy/TheRoad/The_Road', 'r')
# book = file.read()
# doc = nlp(book)
#
# a = bookparser.SentenceLoader()
# #nlp = spacy.load('en_core_web_sm')
# #doc = nlp(u'Apple is looking at buying U.K. startup for $1 billion')
#
# # for token in doc:
# #     print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
# #           token.shape_, token.is_alpha, token.is_stop)
#
# for sent in doc.sents:
#     text = sent.text.rstrip()
#     a.add_sentence(tx, text)

