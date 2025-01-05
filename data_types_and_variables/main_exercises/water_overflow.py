number_of_lines = int(input())

TANK_CAPACITY = 255
total_litres_poured = 0
for _ in range(number_of_lines):
    litres = int(input())
    total_litres_poured += litres

    if total_litres_poured > TANK_CAPACITY:
        print("Insufficient capacity!")
        total_litres_poured -= litres

print(total_litres_poured)