def is_triple_double(word):
    """
    Tests if a word contains three consecutive double letters.

    word: string

    returns: bool
    """
    pass


def find_triple_double():
    """
    Reads a word list and prints words with triple double letters.
    """
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if is_triple_double(word):
            print(word)


print('Here are all the words in the list that have')
print('three consecutive double letters.')
find_triple_double()
print('')
