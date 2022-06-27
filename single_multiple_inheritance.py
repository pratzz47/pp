class Employee:
    def get(self, name, salary, dept):
        self.name = name
        self.dept = dept
        self.salary = salary
    def put(self):
        print("Your name: ",self.name)
        print("Department: ",self.dept)
        print("Salary: ",self.salary)

e = Employee()
e.get(input("Enter name:"), dept = input("Enter department:"), salary=float(input("Enter your salary:")))
e.put()

class Student:
    def get(self):
        self.en = int(input("Enter enrollment no.: "))
        self.name = input("Enter your name:")
        self.dept = input("Enter department:")
class display(Student):
    def display(self):
        print("Enrollment no: ",self.en)
        print("Name: ",self.name)
        print("Department: ",self.dept)

disp = display()
disp.get()
disp.display()
