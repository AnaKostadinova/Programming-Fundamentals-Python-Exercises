divisor = int(input())
boundary = int(input())

max_int = 0

for i in range(1, boundary + 1):
    if i % divisor == 0:
        if i > max_int:
            max_int = i

if i <= boundary:
    print(max_int)