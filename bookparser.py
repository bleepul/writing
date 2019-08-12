import re



class SentenceLoader:

    # Initializer / Instance Attributes
    def __init__(self):
        pass

    @staticmethod
    def add_sentence(tx, text, book):
        text = text.replace('\n', ' ')
        text = text.replace('\'', "\\'")
        text = text.replace('\ ', " ")

        statement = "MATCH (a:Sentence {text: '" + text + "'} ) return a"
        print(statement)
        result = tx.run(statement)

        if len(result.data()) == 0:
            statement = "CREATE (a:Sentence) SET a.text = '" + text + "'"
            tx.run(statement)

            statement = "MATCH(a: Sentence), (b: WrittenWork) \
                         WHERE a.text = '" + text + "' AND b.name = '" + book + "' \
                         CREATE(a) - [r: sentence_in {frequency: 1}]->(b) \
                         RETURN r"
            tx.run(statement)
        else:
            statement = 'MATCH (a:Sentence) - [r: sentence_in]->(b:WrittenWork) \
                            WHERE a.text = "' + text + '" AND b.name = "' + book + '" RETURN a'
            nested_result = tx.run(statement)
            if len(nested_result.data()) == 0:
                statement = "MATCH(a: Sentence), (b: WrittenWork) \
                                         WHERE a.text = '" + text + "' AND b.name = '" + book + "' \
                                         CREATE(a) - [r: sentence_in {frequency: 1}]->(b) \
                                         RETURN r"
                tx.run(statement)
            else:
                statement = 'MATCH (a:Sentence) - [r: sentence_in]->(b:WrittenWork) \
                                                            WHERE a.text = "' + text + '" AND b.name = "' + book + '" set r.frequency = \
                                                            r.frequency + 1 RETURN r.frequency'
                tx.run(statement)

class SentenceGetter:
    @staticmethod
    def get_random_sentence(tx):
        statement = "MATCH(a:Sentence) RETURN a.text, rand() as r ORDER BY r limit 10"
        result = tx.run(statement)
        return result


class Author:
    @staticmethod
    def add(tx, name):
        statement = "MERGE (n:Author {name: '" + name + "'})"
        result = tx.run(statement)
        c = result.summary().counters.nodes_created
        print(c)
        return result


class WrittenWork:
    @staticmethod
    def add(tx, author, name):

        statement = "MERGE(n:WrittenWork {name: '" + name + "'})" \
                    "MERGE(a:Author {name: '" + author + "'})" \
                    "MERGE(n) -[:written_by]-> (a)"
        result = tx.run(statement)
        c = result.summary().counters.nodes_created
        print(c)
        return result


class Sentence:

    counter = 0

    # Initializer / Instance Attributes
    def __init__(self, text, offset=0):
        self.text = text.replace("\n", '').replace('\'', "\\'").replace('\"', "").replace('\ ', " ")
        self.offset = offset

    def add(self, tx, book):
        Sentence.counter = Sentence.counter + 1 + self.offset
        statement = "MERGE(a:WrittenWork {name: '" + book + "'}) " \
                    "MERGE(n:Sentence {text: '" + self.text + "', counter:" + str(Sentence.counter) + "}) " \
                    "MERGE(n) -[:sentence_in]-> (a)"
        result = tx.run(statement)
        return result


class Token:

    total_words = 0
    unique_words = 0


    # Initializer / Instance Attributes
    def __init__(self, text, lemma, pos, tag, dep, shape, is_alpha, is_stop):
        self.text = text.lower()
        self.lemma = lemma
        self.pos = pos
        self.tag = tag
        self.dep = dep
        self.shape = shape
        self.is_alpha = is_alpha
        self.is_stop = is_stop

    def add(self, tx):
        statement = "MERGE(n:Word {text: '" + self.text + "'}) RETURN n"
                    #"MERGE(a:Author {name: '" + author + "'})" \
                    #"MERGE(n) -[:written_by]-> (a)"
        print(self.text)
        result = tx.run(statement)
        c = result.summary().counters.nodes_created

        if c == 0:
            statement = "MATCH(n:Word {text: '" + self.text + "'}) \
                            set n:" + self.pos + " \
                            set n.frequency =  n.frequency + 1 RETURN n"
            Token.total_words = Token.total_words + 1

        else:
            statement = "MATCH(n:Word {text: '" + self.text + "'}) \
                                        set n:" + self.pos + " \
                                        set n.frequency = 1 RETURN n"

            Token.total_words = Token.total_words + 1
            Token.unique_words = Token.unique_words + 1

        result = tx.run(statement)
        # "MERGE(a:Author {name: '" + author + "'})" \
        # "MERGE(n) -[:written_by]-> (a)"
        #print(c)
        return result