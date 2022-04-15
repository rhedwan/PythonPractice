class BodyInfo:
    @staticmethod
    def BMI(weight ,height):
        return weight /(height**2)


print(BodyInfo.BMI(230,6.2))