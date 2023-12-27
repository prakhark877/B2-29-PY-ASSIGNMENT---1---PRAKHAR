input = input("Enter a string: ")

letter_count = 0
digit_count = 0

for char in input:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1

print(f"Alpha -> {letter_count} and number -> {digit_count}")