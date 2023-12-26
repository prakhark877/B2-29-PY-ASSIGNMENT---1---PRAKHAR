def vowel(s) :
    t = s.split()
    count = 0
    for t in s :
        if t=='a' or t=='e' or t=='i' or t=='i' or t=='o' or t=='u' or t=='A' or t=='E' or t=='I' or t=='O' or t=='U' :
            count+=1
    return count
s = str(input())
res = vowel(s)
print(res)