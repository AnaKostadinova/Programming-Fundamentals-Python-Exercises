n = int(input())

for _ in range(n):
    text = input()
    is_valid = False
    for index, value in enumerate(text):
        if value == "," or value == "." or value == "_":
            print(f"{text} is not pure!")
            is_valid = True
            break
    if is_valid == False:
        print(f"{text} is pure.")