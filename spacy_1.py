import spacy

nlp = spacy.load('en_core_web_sm')
# doc = nlp(u'When he woke in the woods in the dark and the cold of the night he\'d reach out to touch the child sleeping beside him. Nights dark beyond darkness and the days more gray each one than what had gone before. Like the onset of some cold glaucoma dimming away the world. His hand rose and fell softly with each precious breath. He pushed away the plastic tarpaulin and raised himself in the stinking robes and blankets and looked toward the east for any light but there was none. In the dream from which he\'d wakened he had wandered in a cave where the child led him by the hand. Their light playing over the wet flowstone walls. Like pilgrims in a fable swallowed up and lost among the inward parts of some granitic beast. Deep stone flues where the water dripped and sang. Tolling in the silence the minutes of the earth and the hours and the days of it and the years without cease. Until they stood in a great stone room where lay a black and ancient lake. And on the far shore a creature that raised its dripping mouth from the rimstone pool and stared into the light with eyes dead white and sightless as the eggs of spiders. It swung its head low over the water as if to take the scent of what it could not see. Crouching there pale and naked and translucent, its alabaster bones cast up in shadow on the rocks behind it. Its bowels, its beating heart. The brain that pulsed in a dull glass bell. It swung its head from side to side and then gave out a low moan and turned and lurched away and loped soundlessly into the dark.')

file = open('Blood_Meridian', 'r')
file2 = open("Blood_Meridian_Vocab", 'w')
book = file.read()
#print(book)

doc = nlp(book)
#for token in doc:
#    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
#          token.shape_, token.is_alpha, token.is_stop)

#for sent in doc.sents:
#    print(sent.text)

vocabulary = []
word_list = []
hash_map = {}

for token in doc:
    if token.text is not u"." and token.text is not u",":
        vocabulary.append(token.text.lower())

for word in vocabulary:
    if word in hash_map:
        hash_map[word] = hash_map[word] + 1
    else:
        hash_map[word] = 1
for key in hash_map.keys():
    print(key + ":          " + str(hash_map[key]))

sorted_by_value = sorted(hash_map.items(), key=lambda kv: kv[1], reverse=True)

for value in sorted_by_value:
    file2.write(str(value[1]) + "\t" + str(value[0]) + "\n")

   # word = str(token)
    #vocabulary_list.append(word.lower())

# my_dict = {i: vocabulary_list.count(i) for i in vocabulary_list}
# word_dist = list(my_dict.keys())
# sorted_dist = word_dist.sort()
# print(my_dict)
# print(word_dist)
    #if word not in vocabulary_list:
#vocabulary_list.sort()
#print(vocabulary_list)
#
# file = open('The Beast.txt', 'r')
# book = file.read()


# def tokenize():
#     if book is not None:
#         words = book.lower().split()
#         return words
#     else:
#         return None


def map_book(tokens):
    hash_map = {}

    if tokens is not None:
        for element in tokens:
            # Remove Punctuation
            #word = element.replace(",", "")
            #word = word.replace(".", "")

            # Word Exist?
            if word in hash_map:
                hash_map[word] = hash_map[word] + 1
            else:
                hash_map[word] = 1

        return hash_map
    else:
        return None


# Tokenize the Book
#words = tokenize()
#word_list = ['the', 'life', 'situations', 'since', 'day']

# Create a Hash Map (Dictionary)
# map = map_book(vocabulary_list)
#
# # Show Word Information
# for word in vocabulary_list:
#     print('Word: [' + word + '] Frequency: ' + str(map[word]))