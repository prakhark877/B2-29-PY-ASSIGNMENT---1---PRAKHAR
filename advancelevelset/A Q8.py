def userdata( s):
    new_s = s.split('0')
    l = [ ele for ele in new_s if len(ele) !=0]
    d = {"first_name" :  l[0] , "last_name":l[1] , "id":l[2]}
    return d 
 
s = input()
print(userdata(s))
