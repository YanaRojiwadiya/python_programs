"""Assignment 1: Word Counter

Create a Python script that reads a text file and counts the frequency of each word in the file.
Store the word frequencies in a dictionary.
Print out the top 5 most common words and their frequencies."""

with open('example.txt', 'r') as file:
    a = file.read()
words = a.split()
frequencies = {}

for i in words:
    frequencies[i] = frequencies.get(i, 0) + 1
    # if i in frequencies:
    #     frequencies[i] += 1
    # else:
    #     frequencies[i] = 1

sorting = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)

for w, f in sorting[:5]:
    print(f'{w}: {f}')
