class Employee:
    def __init__(self, ID=None, salary=0, department=None) :
        self.ID = ID
        self.salary =salary
        self.department = department

    def tax(self):
        return self.salary *0.2
    
    def salaryPerDay(self):
        return self.salary / 30


Mark = Employee(23424, 240000, "Human Resources")

print("ID: ", Mark.ID)
print("Salary: ", Mark.salary)
print("Department: ",Mark.department )
print("Tax: ",Mark.tax())
print("Salary Per day: ",Mark.salaryPerDay())