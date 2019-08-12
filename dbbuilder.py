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
    def __init__(self, tx, work, sent, offset=0):
        self.text = sent.text.replace("\n", '').replace('\'', "\\'").replace('\"', "").replace('\ ', " ")
        self.offset = offset
        self.sent = sent
        self.sentence = []
        self.sentence_structure = []
        self.sentence_structure_detailed = []
        self.process_sentence(tx)

        self.add(tx, work)

    def add(self, tx, book):
        Sentence.counter = Sentence.counter + 1 + self.offset
        statement = "MERGE(a:WrittenWork {name: '" + book + "'})  \
                        MERGE(n:Sentence {text: '" + self.text + "', \
                        sentence: " + str(self.sentence) + ", \
                        sentence_structure: " + str(self.sentence_structure) + ", \
                        sentence_structure_detailed: " + str(self.sentence_structure_detailed) + ", \
                        position:" + str(Sentence.counter) + "})  \
                    MERGE(n) -[:sentence_in]-> (a)"
        result = tx.run(statement)
        return result

    def process_sentence(self, tx):
        for token in self.sent:
            if token.tag_ == '' or token.tag_ == "_SP":
                pass
            else:
                t = Token(token)
                t.add(tx)
                self.sentence.append(token.text)
                self.sentence_structure.append(token.pos_)
                self.sentence_structure_detailed.append(token.tag_)


class Token:

    total_words = 0
    unique_words = 0

    # Initializer / Instance Attributes
    def __init__(self, token):
        self.text = token.text.replace("\n", '').replace('\'', "\\'").replace('\"', "").replace('\ ', " ").lower()
        self.lemma = token.lemma_
        self.pos = token.pos_
        self.tag = token.tag_
        self.dep = token.dep_
        self.shape = token.shape_
        self.is_alpha = token.is_alpha
        self.is_stop = token.is_stop

    def add(self, tx):
        statement = "MERGE(n:Word {text: '" + self.text + "'}) RETURN n"
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
        return result
