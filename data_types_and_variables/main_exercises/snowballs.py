snowballs_number = int(input())

highest_snowball_value = 0
highest_weight = 0
highest_snowball_time_to_target = 0
highest_snowball_quality = 0
for i in range(snowballs_number):
    snowball_weight = int(input())
    snowball_time_to_target = int(input())
    snowball_quality = int(input())

    current_snowball_value = (snowball_weight // snowball_time_to_target) ** snowball_quality
    if current_snowball_value > highest_snowball_value:
        highest_snowball_value = current_snowball_value
        highest_weight = snowball_weight
        highest_snowball_time_to_target = snowball_time_to_target
        highest_snowball_quality = snowball_quality

print(f"{highest_weight} : {highest_snowball_time_to_target} = {highest_snowball_value} ({highest_snowball_quality})")