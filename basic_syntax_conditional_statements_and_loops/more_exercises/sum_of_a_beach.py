from itertools import count

text = input()

counter = 0
text = text.lower()

if "water" in text:
    counter += text.count("water")
if "sand" in text:
    counter += text.count("sand")
if "fish" in text:
    counter += text.count("fish")
if "sun" in text:
    counter += text.count("sun")

print(counter)