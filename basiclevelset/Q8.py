def calculate_lcm(a, b):
    def calculate_gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    gcd = calculate_gcd(a, b)
    lcm = (a * b) // gcd

    return lcm

number1 = 12
number2 = 18

result = calculate_lcm(number1, number2)

print(f"LCM of {number1} and {number2} is: {result}")