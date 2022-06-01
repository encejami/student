class Student:
    def __init__(self,name,grade1,grade2,grade3):
        self.name=name
        self.grade1=grade1
        self.grade2=grade2
        self.grade3=grade3

    def sum (self):
        return self.grade1+self.grade2+self.grade3

    def average (self):
        return self.sum()/3

    def massege (self):
            print("hello")
            return(f"Your Name is {self.name} and your avrage is : {self.average}")

s=Student("saleh", 20, 50, 70)

print(s.sum())
print(s.average())
print(s.massege())
