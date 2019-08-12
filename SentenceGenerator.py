import numpy as np
import random
import sys

outfile = open("Thatcher Reed", 'w')

number_of_chapters = random.randint(25,40)

for c in range(number_of_chapters):
    outfile.write("Chapter " + str(c+1) + ".\n\n")

    number_of_paragraphs = random.randint(30,60)

    for p in range(number_of_paragraphs):
        dialogue_block = random.randint(0, 2)
        outfile.write(str(p+1) + ". ")
        if dialogue_block > 0:
            number_of_sentences = random.randint(1,10)

            for a in range(number_of_sentences):
                y = ["B"]
                L = np.random.normal(3, 5)
                number_of_clauses = abs(int(L))
                for x in range(number_of_clauses):

                    left_right = random.randint(0,3)
                    has_subordinate = random.randint(0, 3)
                    clause_code = str(random.randint(1, 10))

                    if left_right == 0:
                        if has_subordinate > 1:
                            y.insert(0, "{S" + str(random.randint(1, 3)) + "}")
                        y.insert(0, "C" + clause_code)

                    else:
                        y.append("C" + clause_code)
                        if has_subordinate > 1:
                            y.append("{S" + str(random.randint(1, 3)) + "}")

                str1 = ''.join(y)
                outfile.write("\t" + str1 + ".\n")
            outfile.write("\n\n")
        else:
            outfile.write("DIALOGUE BLOCK")
            outfile.write("\n\n")
