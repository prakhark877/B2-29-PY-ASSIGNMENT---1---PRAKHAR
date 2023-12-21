def test(n):
    return [n + 2 * i for i in range(n)]
n = 7
print(test(n))
open_file = open("demo.txt","r")
count  = 0
text = open_file.read()
list = text.split("\n")
for x in list:
    if x:
        count += 1
print("Total number of lines in the text file are:", count )
