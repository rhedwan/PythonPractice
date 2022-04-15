class Employee:
    def __init__(self, ID=None, salary=0, department=None) :
        self.ID = ID
        self.salary =salary
        self.department = department

Mark = Employee()
Steve = Employee(23424, 240000, "Human Resources")

print("ID: ", Mark.ID)
print("Salary: ", Mark.salary)
print("Department: ",Mark.department )

print("ID: ", Steve.ID)
print("Salary: ", Steve.salary)
print("Department: ",Steve.department )

