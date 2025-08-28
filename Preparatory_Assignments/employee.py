# Q11: Employee structure using class
class Employee:
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
    
    def yearly_salary(self):
        return self.salary * 12
    
    def raise_salary(self, percent):
        self.salary += self.salary * percent / 100
    
    def display(self):
        print(f"{self.fname} {self.lname}, Salary: {self.salary}")

# Test
e1 = Employee("John", "Doe", 3000)
e2 = Employee("Jane", "Smith", 4000)

print("Yearly Salary:")
print(e1.fname, ":", e1.yearly_salary())
print(e2.fname, ":", e2.yearly_salary())

e1.raise_salary(10)
e2.raise_salary(10)

print("\nAfter 10% raise:")
print(e1.fname, ":", e1.yearly_salary())
print(e2.fname, ":", e2.yearly_salary())
