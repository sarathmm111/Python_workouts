def break_words(sentence):
    """Breaks words in a sentence."""
    return sentence.split(' ')

def sort_words(words):
    """Sorts the words in a list."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Sorts the words in a sentence."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of a sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words in a sentence and prints the first and last."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
