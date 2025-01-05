from itertools import count

number_of_lines = int(input())

brackets = ""
counter = 0
for _ in range(number_of_lines):
    line = input()
    if line == '(' or line == ')':
        brackets += line

balanced_line = brackets.replace("()", "")
if balanced_line == "":
    print("BALANCED")
else:
    print("UNBALANCED")