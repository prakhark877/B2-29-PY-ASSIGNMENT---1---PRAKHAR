def cmp(next,set):
    data = {}
    cntent = 0
    for e in set:
        if e not in data:
            if (len(data)>next):
                cntent += 1 
            data[e] = 1
        else:
            # print(d)
            if (len(data) > next):
                cntent += 1
                print(f"person is {e}")
            del data[e]
            # print(d)

    return cntent
next = int(input())
set = input()
print(f"number of person not using computer are : {cmp(next,set)}")
