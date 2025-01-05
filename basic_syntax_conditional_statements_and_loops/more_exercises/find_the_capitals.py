text = input()

letters = []

for index, value in enumerate(text):
    if value.isupper():
        letters.append(index)

print(letters)