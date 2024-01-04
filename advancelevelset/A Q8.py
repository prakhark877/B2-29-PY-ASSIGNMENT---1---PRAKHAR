def func(tr):
    new = tr.split('0')
    ltr = [ e for e in new if len(e)!=0]
    data = {"first_name" :  ltr[0] , "last_name":ltr[1] , "id":ltr[2]}
    return data

tr = input()
print(func(tr))
