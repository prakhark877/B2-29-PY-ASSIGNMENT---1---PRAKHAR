#single inheritance
class College: 
    def College_detail(self):
        print("I am from College")
class Student(College):
    def student_detail( self):
        print("I am from Student")


b = Student()
b.student_detail()
b.College_detail()

#multiple inheritance
class First:
    def __init__(self,first):
        self.first =first 

class Second:
    def __init__(self,second):
        self.second = second 
    
class Add ( First, Second):
    def __init__(self,first,second ):
        First.__init__(self,first)
        Second.__init__(self,second)
    
    def addition(self):
        print(self.first + self.second)
res = Add(1,3)
res.addition()


#multilevel
class GrandParentCompany:
    def __init__(self,grand_name):
        self.grand_name = grand_name 

class ParentCompany(GrandParentCompany):
    def __init__(self,par_name,grand_name):
        self.par_name = par_name 
        GrandParentCompany.__init__(self,grand_name)

class ChildCompany( ParentCompany):
    def __init__(self,grad_name,par_name,child_name):
        self.child_name = child_name 
        ParentCompany.__init__(self,par_name,grad_name)
    def print_detail(self):
        print(f"Grand Parent Company : {self.grand_name} Parent Company: {self.par_name} Child Company: {self.child_name}")

c = ChildCompany("Alphabet","Google","Chrome")
c.print_detail()
