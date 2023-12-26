def student(name,subject):
        # d  = {}
        # for n,s in zip(name,subject):
        #         if n not in d :
        #             d[n] = s 
        # return d 
        return {n:s for n,s in zip( name, subject)}
     


name = input().split()
subject = input().split()
print(student(name, subject))
