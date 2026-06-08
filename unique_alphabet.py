lowercase_words = []

def unique_alphabet(words):

    for word in words:
        lowercase_words.append(word.lower())

    unique_word = set(lowercase_words)
    ordered_word = sorted(unique_word)

    print("Ordered Word Alphabetically:")
    for words in ordered_word:
        print("-",words)

first_sentence = "It is a threat, Yes it is a threat."
list_of_words = first_sentence.split()
print("Test 1")
unique_alphabet(list_of_words)
print()

second_sentence = "Python is fun, and coding in python is great"
list_of_words_two = second_sentence.split()
print("Test 2")
unique_alphabet(list_of_words_two)
