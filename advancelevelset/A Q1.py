
try:
    fi = open("cmm.txt","w")
    k1 = "Hello,how are you!"
    k2 =  "Are you alright?"
    k3 = "Can I help you?"
    fi.write(k1 + "\n")
    fi.write(k2 + "\n")
    fi.write(k3)
    fi.close()

    fi  = open("cmm.txt","r")
    wo = fi.read()
    split_word = wo.split()
    res = []
    for e in split_word:
        if len(e) % 2 == 0:
            res.append(e)
    ans = " ".join(res)
    print(f"string of even length: {ans}")
except FileNotFoundError:
    print("not found")
