try:
    file = open("doc.txt","w")
    a = "Hello I am a file"
    b =  "Where you need to return the data string"
    c = "Which is of even length"
    file.write(a + "\n")
    file.write(b + "\n")
    file.write(c)
    file.close()

    file  = open("doc.txt","r")
    w = file.read()
    split_words =w.split()
    r = []
    for e in split_words:
        if len(e) % 2 == 0:
            r.append(e)
    ans = " ".join(r)
    print(f"string of even length: {ans}")
except FileNotFoundError:
    print("not found")
