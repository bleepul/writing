def test_and_increment(element, list, freq_hash):
    if element not in list:
        list.append(element)
        freq_hash[element] = 1
    else:
        freq_hash[element] = freq_hash[element] + 1


def test_and_increment_pos(element, list, freq_hash, token, pos):
    if element not in list and token == pos:
        list.append(element)
        freq_hash[element] = 1
    elif element in list and token == pos:
        freq_hash[element] = freq_hash[element] + 1


def reverse_sort_and_print_hash_to_file(the_hash, filename):
    outfile1 = open(filename, 'w')
    sorted_hash = sorted(the_hash.items(), key=lambda kv: kv[1], reverse=True)
    for v in sorted_hash:
        print(str(v[1]) + "\t" + str(v[0]))
        outfile1.write(str(v[1]) + "\t" + str(v[0]) + "\n")
    outfile1.close()
    return
