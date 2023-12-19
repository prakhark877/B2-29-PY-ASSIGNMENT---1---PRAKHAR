def check(s1,s2) :
    if sorted(s1) == sorted(s2) :
        print("Anagrams")
    else :
        print("Not Anagrams")
s1 = "listen"
s2 = "silent"
check(s1,s2)