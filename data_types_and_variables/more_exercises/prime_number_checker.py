number = int(input())
is_prime = False
counter = 0
for num in range(2, number + 1):
    if number % num == 0:
        counter += 1

if counter == 1:
    is_prime = True

print(is_prime)