from neo4j import GraphDatabase
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', help='flag')
parser.add_argument('-a', help='author')
parser.add_argument('-w', help='work')
args = parser.parse_args()

uri = "bolt://localhost:7687"
d = GraphDatabase.driver(uri, auth=("neo4j", "password"))
txn = d.session()


def get_random_sentence(tx):
    statement = "MATCH(s:Sentence) -[:sentence_in]-> (w:WrittenWork) -[:written_by]-> (a:Author) RETURN w.name, \
                    s.sentence_structure, rand() as r ORDER BY r limit 10"
    result = tx.run(statement)
    return result

def get_random_sentence_by_author(tx, author):
    statement = "MATCH(s:Sentence) -[:sentence_in]-> (w:WrittenWork) -[:written_by]-> (a:Author)  \
                   where a.name = '" + author + "' RETURN w.name, s.sentence_structure, rand() as r ORDER BY r limit 10"
    result = tx.run(statement)
    return result


def get_random_sentence_by_work(tx, work):
    statement = "MATCH(s:Sentence) -[:sentence_in]-> (w:WrittenWork) -[:written_by]-> (a:Author)  \
                where w.name = '" + work + "' RETURN w.name, s.sentence_structure, rand() as r ORDER BY r limit 10"
    result = tx.run(statement)
    return result


if args.f == "all":
    s = get_random_sentence(txn)
    for r in s:
        print(str(r[0]) + " : " + str(r[1]))

if args.f == "author":
    s = get_random_sentence_by_author(txn,args.a)
    for r in s:
        print(str(r[0]) + " : " + str(r[1]))

if args.f == "work":
    s = get_random_sentence_by_work(txn,args.w)
    for r in s:
        print(str(r[0]) + " : " + str(r[1]))

