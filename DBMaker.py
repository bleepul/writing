import spacy
from neo4j import GraphDatabase
import argparse, sys
import dbbuilder

nlp = spacy.load('en_core_web_sm')

uri = "bolt://localhost:7687"
d = GraphDatabase.driver(uri, auth=("neo4j", "password"))
tx = d.session()

parser = argparse.ArgumentParser()
parser.add_argument('--author', help='Do the bar option')
parser.add_argument('--work', help='Foo the program')
args = parser.parse_args()

a = text = args.author.replace(' ', '')
b = text = args.work.replace(' ', '')
path = "Books/" + a + "/" + b

print(args.author)
print(args.work)
print(path)

file = open(path, 'r')
book = file.read()

dbbuilder.WrittenWork.add(tx,  args.author, args.work,)
doc = nlp(book)

for sent in doc.sents:
    s = dbbuilder.Sentence(tx, args.work, sent)




