strr = "shhhaaakk"
l2 = []
newstr = ""
count = 1
for i in range(len(strr)-1):

    if strr[i] == strr[i+1]:
        count+=1
    else:
        newstr = newstr + strr[i] + str(count)
        count = 1
newstr = newstr + strr[-1] + str(count)


print(newstr)