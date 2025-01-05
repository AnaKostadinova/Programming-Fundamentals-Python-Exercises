text = input()

reversed_word = ""

for i in range(len(text) - 1, -1, -1):
    reversed_word += text[i]

print(reversed_word)


# text = input()
#
# for letter in reversed(text):
#     print(letter, end="")