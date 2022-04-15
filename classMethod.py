class MyDomain:

    classVariable = "Educative"

    @classmethod
    def demo(cls):
        return cls.classVariable

    @staticmethod
    def demoInfo():
        print("Here's a static method")


test = MyDomain()
print(test.demoInfo())

print(MyDomain.demo())