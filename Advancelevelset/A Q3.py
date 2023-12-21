def JTOI(data):
    try : 
        #write content in file
        file = open("WORDS.txt","w" )
        file.write(data)
        file.close()

        #read
        file = open("WORDS.txt","r")
        content  = file.read()
        res = "" 
        content = content.replace("j","i")
        content  = content.replace("J","I")
        res += content 
        return res  

    except FileNotFoundError:
        return "file not found"
data = input()
print(JTOI(data))
    
