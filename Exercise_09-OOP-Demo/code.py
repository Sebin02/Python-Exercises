#create an Employee class to show property decorator
class Employee:
    def __init__(self,first,last):
        self.first=first
        self.last=last

    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first.lower(),self.last.lower())
    
    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self,name):
        first, last=name.split(' ')
        self.first=first
        self.last=last

    @fullname.deleter
    def fullname(self):
        print("Delete name")
        self.first=None
        self.last=None

emp_1=Employee("John","Doe")

emp_1.fullname="Jane Smith"
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del  emp_1.fullname