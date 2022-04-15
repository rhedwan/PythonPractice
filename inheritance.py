class Student:
    maxAge = 20
    def __init__(self,name, age, disability):
        self.disability =disability
        self.age = age
        self.name = name

    def displayBio(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Disabiliy: ", self.disability)
    

class Prefect(Student):
    maxAge = 16
    def __init__(self,name, age, disability, post):
        # Student.__init__(self,name, age, disability)
        super().__init__(name, age, disability)
        self.post = post

    def displayStatus(self):
        self.displayBio()
        print("Post Held: ",self.post)

    def publicUpdate(self):
        print("Age limit for student: ", super().maxAge)
        print("Age limit for prefect: ", self.maxAge)


s1 = Prefect("Bryan", 23, False, "Head Boy")
s1.displayStatus()
s1.publicUpdate()