userSentence = input("Enter a sentence: ")
words = userSentence.lower().split()

word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print("\nDuplicate words:")
for word in word_counts:
    if word_counts[word] > 1:
        print(f"'{word}' appears {word_counts[word]} times")
