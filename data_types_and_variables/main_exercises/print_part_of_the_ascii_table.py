first_chr_index = int(input())
last_chr_index = int(input())

for i in range(first_chr_index, last_chr_index + 1):
    print(chr(i), end=" ")