def func(text):
    try :
        #write content in file
        make = open("WORDS.txt","w" )
        make.write(text)
        make.close()

        #read
        make = open("WORDS.txt","r")
        cont  = make.read()
        out = ""
        cont = cont.replace("j","i")
        cont  = cont.replace("J","I")
        out += cont
        return out

    except FileNotFoundError:
        return "file not found"
text = input()
print(func(text))
