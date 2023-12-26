def func(s) :
    if s%3==0 :
        print('Brudite')
    if s%5==0 :
        print('Python Training')
    if s%3==0 and s%5==0 :
        print('Brudite - Python Training')

s = int(input('Enter a number'))
func(s)
