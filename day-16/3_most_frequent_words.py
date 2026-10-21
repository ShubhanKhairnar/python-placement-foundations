text = input("Enter a sentence: ")
words = text.lower().split()

counts = {}

for word in words:
    counts[word] = counts.get(word, 0) + 1

top_words = sorted(
    counts.items(),
    key=lambda item: (-item[1], item[0])
)[:3]

for word, frequency in top_words:
    print(f"{word}: {frequency}")