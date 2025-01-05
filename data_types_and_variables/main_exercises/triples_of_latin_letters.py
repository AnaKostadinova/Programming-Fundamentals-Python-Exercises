first_three_letters = int(input())

for i in range(97, 97 + first_three_letters):
    for j in range(97, 97 + first_three_letters):
        for k in range(97, 97 + first_three_letters):
            print(f"{chr(i)}{chr(j)}{chr(k)}")