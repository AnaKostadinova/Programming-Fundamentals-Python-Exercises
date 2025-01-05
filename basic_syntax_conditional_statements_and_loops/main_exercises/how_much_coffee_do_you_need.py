coffee_needed = 0
while True:
    text = input()
    if text == "END":
       break
    if text == "coding" or text == "cat" or text == "dog" or text == "movie":
            coffee_needed += 1
    elif text == "CODING" or text == "CAT" or text == "DOG" or text == "MOVIE":
            coffee_needed += 2
    else:
        continue

if coffee_needed <= 5:
    print(f"{coffee_needed}")
else:
    print("You need extra sleep")