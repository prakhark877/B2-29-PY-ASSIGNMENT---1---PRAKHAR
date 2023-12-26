def without_using_comp(n,s):
    d = {}
    cnt = 0
    for ele in s:
        if ele not in d:
            if (len(d)>n):
                cnt += 1 
            d[ele] = 1
        else:
            # print(d)
            if (len(d) >n):
                cnt += 1
                print(f"person is {ele}")
            del d[ele]
            # print(d)

    return cnt
n = int(input())
s = input()
print(f"number of person without using the computer are: {without_using_comp(n,s)}")
