import spacy
import bracy

nlp = spacy.load('en_core_web_sm')

file = open('HGWELLS_IoDM', 'r')
book = file.read()
doc = nlp(book)

prefix = "HGWELLS_IoDM"
outfile = open(prefix + "_sentences", 'w')

vocabulary, pos, tag, dep, combo, noun, verb = [], [], [], [], [], [], []
word_freq, pos_freq, tag_freq, dep_freq, combo_freq, noun_freq, verb_freq = {}, {}, {}, {}, {}, {}, {}

DET, ADP, PUNCT, ADJ, PRON, CCONJ, ADV, PART, PROPN, SPACE, NUM, INTJ, X, SYM = [],  [],  [],  [],  [],  [],  [],  [],  [],  [],  [],  [],  [],  []

DET_freq, ADP_freq, PUNCT_freq, ADJ_freq, PRON_freq, CCONJ_freq, ADV_freq, PART_freq, PROPN_freq, SPACE_freq, NUM_freq, INTJ_freq, X_freq, SYM_freq = {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}

for sent in doc.sents:

    outfile.write(sent.text.rstrip() + "\t")
    structure = []

    for token in sent:
        word = token.text.lower()
        if word != "": structure.append(str(token.pos_))
        combination = str(token.pos_) + " " + str(token.tag_) + " " + str(token.dep_)

        bracy.test_and_increment(word, vocabulary, word_freq)
        bracy.test_and_increment(token.pos_, pos, pos_freq)
        bracy.test_and_increment(token.tag_, tag, tag_freq)
        bracy.test_and_increment(token.dep_, dep, dep_freq)
        bracy.test_and_increment(combination, combo, combo_freq)

        bracy.test_and_increment_pos(word, noun, noun_freq, token.pos_, "NOUN")
        bracy.test_and_increment_pos(word, verb, verb_freq, token.pos_, "VERB")
        bracy.test_and_increment_pos(word, DET, DET_freq, token.pos_, "DET")
        bracy.test_and_increment_pos(word, ADP, ADP_freq, token.pos_, "ADP")
        bracy.test_and_increment_pos(word, PUNCT, PUNCT_freq, token.pos_, "PUNCT")
        bracy.test_and_increment_pos(word, ADJ, ADJ_freq, token.pos_, "ADJ")
        bracy.test_and_increment_pos(word, PRON, PRON_freq, token.pos_, "PRON")
        bracy.test_and_increment_pos(word, CCONJ, CCONJ_freq, token.pos_, "CCONJ")
        bracy.test_and_increment_pos(word, ADV, ADV_freq, token.pos_, "ADV")
        bracy.test_and_increment_pos(word, PART, PART_freq, token.pos_, "PART")
        bracy.test_and_increment_pos(word, PROPN, PROPN_freq, token.pos_, "PROPN")
        bracy.test_and_increment_pos(word, SPACE, SPACE_freq, token.pos_, "SPACE")
        bracy.test_and_increment_pos(word, NUM, NUM_freq, token.pos_, "NUM")
        bracy.test_and_increment_pos(word, INTJ, INTJ_freq, token.pos_, "INTJ")
        bracy.test_and_increment_pos(word, X, X_freq, token.pos_, "X")
        bracy.test_and_increment_pos(word, SYM, SYM_freq, token.pos_, "SYM")


    outfile.write(','.join(structure) + "\n")


bracy.reverse_sort_and_print_hash_to_file(word_freq, prefix + "_word_freq")
bracy.reverse_sort_and_print_hash_to_file(pos_freq, prefix + "_pos_freq")
bracy.reverse_sort_and_print_hash_to_file(tag_freq, prefix + "_tag_freq")
bracy.reverse_sort_and_print_hash_to_file(dep_freq, prefix + "_dep_freq")
bracy.reverse_sort_and_print_hash_to_file(combo_freq, prefix + "_combo_freq")
bracy.reverse_sort_and_print_hash_to_file(noun_freq, prefix + "_noun_freq")
bracy.reverse_sort_and_print_hash_to_file(verb_freq, prefix + "_verb_freq")

bracy.reverse_sort_and_print_hash_to_file(DET_freq,prefix + "_DET_freq")
bracy.reverse_sort_and_print_hash_to_file(ADP_freq,prefix + "_ADP_freq")
bracy.reverse_sort_and_print_hash_to_file(PUNCT_freq,prefix + "_PUNCT_freq")
bracy.reverse_sort_and_print_hash_to_file(ADJ_freq,prefix + "_ADJ_freq")
bracy.reverse_sort_and_print_hash_to_file(PRON_freq,prefix + "_PRON_freq")
bracy.reverse_sort_and_print_hash_to_file(CCONJ_freq,prefix + "_CCONJ_freq")
bracy.reverse_sort_and_print_hash_to_file(ADV_freq,prefix + "_ADV_freq")
bracy.reverse_sort_and_print_hash_to_file(PART_freq,prefix + "_PART_freq")
bracy.reverse_sort_and_print_hash_to_file(PROPN_freq,prefix + "_PROPN_freq")
bracy.reverse_sort_and_print_hash_to_file(SPACE_freq,prefix + "_SPACE_freq")
bracy.reverse_sort_and_print_hash_to_file(NUM_freq,prefix + "_NUM_freq")
bracy.reverse_sort_and_print_hash_to_file(INTJ_freq,prefix + "_INTJ_freq")
bracy.reverse_sort_and_print_hash_to_file(X_freq,prefix + "_X_freq")
bracy.reverse_sort_and_print_hash_to_file(SYM_freq, prefix + "_SYM_freq")
