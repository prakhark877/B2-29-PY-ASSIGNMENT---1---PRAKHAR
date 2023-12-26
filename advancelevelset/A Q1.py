
try:
    file = open("doc.txt","w")
    k1 = "Hello I am a file"
    k2 =  "Where you need to return the data string"
    k3 = "Which is of even length"
    file.write(k1 + "\n")
    file.write(k2 + "\n")
    file.write(k3)
    file.close()

    file  = open("doc.txt","r")
    word = file.read()
    split_wo =word.split()
    res = []
    for e in split_wo:
        if len(e) % 2 == 0:
            res.append(e)
    ans = " ".join(res)
    print(f"string of even length: {ans}")
except FileNotFoundError:
    print("not found")
