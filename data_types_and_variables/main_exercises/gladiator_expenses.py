lost_fight_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armour_price = float(input())

broken_helmet_counter = 0
broken_sword_counter = 0
broken_shield_counter = 0
broken_armour_counter = 0
broken_shield_counter_increase = False
for i in range(1, lost_fight_count + 1):
    broken_shield_counter_increase = False
    if i % 2 == 0:
        broken_helmet_counter += 1
    if i % 3 == 0:
        broken_sword_counter += 1
    if i % 2 == 0 and i % 3 == 0:
        broken_shield_counter += 1
        broken_shield_counter_increase = True
    if broken_shield_counter % 2 == 0 and broken_shield_counter_increase == True:
        broken_armour_counter += 1

total_cost = ((broken_helmet_counter * helmet_price) + (broken_sword_counter * sword_price)
              + (broken_shield_counter * shield_price) + (broken_armour_counter * armour_price))
print(f"Gladiator expenses: {total_cost:.2f} aureus")