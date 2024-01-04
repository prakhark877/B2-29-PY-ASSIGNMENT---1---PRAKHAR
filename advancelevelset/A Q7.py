def func(na,sub): 
        return {i:j for i,j in zip( na, sub)}
     


na = input().split()
sub = input().split()
print(func(na,sub))
