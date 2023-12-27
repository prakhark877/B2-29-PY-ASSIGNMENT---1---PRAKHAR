def J(data):
    try : 
        #write content in file
        file = open("WORDS.txt","w" )
        file.write(data)
        file.close()

        #read
        file = open("WORDS.txt","r")
        con  = file.read()
        res = "" 
        con = con.replace("j","i")
        con  = con.replace("J","I")
        res += con
        return res  

    except FileNotFoundError:
        return "file not found"
data = input()
print(J(data))
    
