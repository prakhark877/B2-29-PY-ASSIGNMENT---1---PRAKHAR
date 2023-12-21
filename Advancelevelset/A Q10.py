def without_using(m,s):
    x = {}
    cnt = 0
    for e in s:
        if e not in x:
            if (len(x)>n):
                cnt += 1 
            x[e] = 1
        else:
            # print(d)
            if (len(x) >n):
                cnt += 1
                print(f"person is {e}")
            del x[e]
            # print(d)

    return cnt
m = int(input())
s = input()
print(f"number of person without using the computer are: {without_using(m,s)}")
