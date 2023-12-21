def user(x):
    new = x.split('0')
    l = [ e for e in new if len(e) !=0]
    f = {"first_name" :  l[0] , "last_name":l[1] , "id":l[2]}
    return f 
 
x = input()
print(user(x))
