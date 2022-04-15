class MyClass:
    pass

obj = MyClass()
print(obj)

# By Initializing
class Employee:
    ID = 3434
    salary =340040
    department = "Human Resources"

Steve = Employee()
print("ID: ", Steve.ID)
print("Salary: ", Steve.salary)
print("Department: ",Steve.department )

# By Assigning
class _Employee:
    ID = None
    salary = None
    department = None


Jack = _Employee()
Jack.ID = 2300
Jack.salary = 35303
Jack.department = "Software Eng"
Jack.title = "CEO"

print("ID: ", Jack.ID)
print("Salary: ", Jack.salary)
print("Department: ",Jack.department )
print("Title: ",Jack.title )