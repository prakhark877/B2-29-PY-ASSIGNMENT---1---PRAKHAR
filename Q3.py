s = int(input("Enter marks of physics : "))
t = int(input("Enter marks of chemistry : "))
u = int(input("Enter marks of biology : "))
v = int(input("Enter marks of mathematics : "))
w = int(input("Enter marks of computer : "))
avg = (s+t+u+v+w)/5
print(avg)
if avg>=90 :
    print("Grade A")
elif avg>=80 :
    print("Grade B")
elif avg>=70 :
    print("Grade C")
elif avg>=60 :
    print("Grade D")
elif avg>=40 :
    print("Grade E")
elif avg<40 :
    print("Grade F")