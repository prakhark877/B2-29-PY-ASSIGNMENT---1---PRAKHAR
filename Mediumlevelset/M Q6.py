def power(num):
    if num == 1:
        print("Power of two")

    elif num%2!=0:
        print("Not power of two")

    else:
        num = num//2
        power(num)

num = 32
power(num)