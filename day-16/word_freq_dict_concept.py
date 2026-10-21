text = input("Enter a sentence: ")
words = text.lower().split()

#Create an empty dictionary
counts = {}
#Think of counts as a scoreboard. Each word is a key, and its frequency is the value.

for word in words:
    counts[word] = counts.get(word,0)+1


#for word in words: — takes each word from the list, one at a time.
#counts.get(word, 0) — gets the current count for that word, or 0 if it's not in the dictionary yet.
#+ 1 — increases the count by one.
#counts[word] = ... — saves the updated count in the dictionary.

    print(counts)
    