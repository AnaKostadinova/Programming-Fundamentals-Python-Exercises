n = int(input()) + 1

while True:
    a = set(str(n))
    b = list(str(n))
    if len(b) == len(a):
        print(n)
        break
    n = int(n) + 1