key = int(input())
number_of_characters = int(input())

message = ""
for _ in range(number_of_characters):
    character = input()
    new_character = key + ord(character)
    message += chr(new_character)

print(message)