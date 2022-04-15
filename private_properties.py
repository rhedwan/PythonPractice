class Employee:
    def __init__(self, ID,salary):
        self.ID = ID
        self.__salary =  salary

    def displaySalary(self):
        print("Salary:", self.__salary)

    def __displayID(self):
        print("ID: ", self.ID)



steve = Employee(2344, 25235)
print("ID:", steve.ID)
# print(steve.__salary)
steve.displaySalary()
# steve.__displayID()