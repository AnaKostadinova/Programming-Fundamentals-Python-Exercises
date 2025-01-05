while True:
    text = input()

    if text == "End":
        break
    if text == "SoftUni":
        continue
    for index, value in enumerate(text):
        print(f"{value * 2}", end="")
    print("")