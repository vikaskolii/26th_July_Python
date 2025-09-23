from collections import Counter

sentence = "Python is great and Python is easy"
words = sentence.lower().split()
freq = Counter(words)
print(freq)
