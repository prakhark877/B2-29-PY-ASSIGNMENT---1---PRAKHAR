def sum_of_digits(num):
    while num >= 10:
        digit_sum = 0
        while num > 0:
            digit_sum += num % 10
            num //= 10

        num = digit_sum

    return num

sample_input = 9876
result = sum_of_digits(sample_input)

print(f"Sample Input: num = {sample_input}")
print(f"Sample Output: Sum_of_digits = {result}")