def total(x):
    r = []
    j = 0
    for i in range(x):

        r.append(x+j)
        j+=2 
    return r 
x = int(input())
print(total(x))
