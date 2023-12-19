start = int(input("Enter the start number: "))
stop = int(input("Enter the stop number: "))

sum = 0

for number in range(start, stop + 1):
    if number % 2 != 0:
        sum+= number

print(f"Sum of odd numbers between {start} and {stop}: {sum}")