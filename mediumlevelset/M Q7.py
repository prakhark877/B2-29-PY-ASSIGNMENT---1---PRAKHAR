a = [7, 2, 5, 1, 9, 3]
a.sort()
if len(a)%2!=0:
    med = a[len(a)//2]

else:
    med = (a[len(a)//2] + a[len(a)//2 - 1])/2
print(med)