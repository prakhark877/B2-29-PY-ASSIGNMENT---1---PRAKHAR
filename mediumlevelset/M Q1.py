def common(l1,l2) :
    s1 = set(l1)
    s2 = set(l2)
    if(s1 & s2) :
        print(list(s1 & s2))
    else :
        print("No common memmbers")
l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7, 8]
common(l1,l2)
