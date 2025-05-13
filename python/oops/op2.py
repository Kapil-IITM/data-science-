# creating student records 

# class - Blueprint or template 

class Student:
    def __init__(self,name,grade,percentage): # __init__ method->> constructor value initialize
        # self parameter - refrence or connection build btw class and object
        self.name = name # attribute 
        self.grade = grade # attribute 
        self.percentage = percentage

    def Student_details(self): # method 
        print(f"{self.name} is in class {self.grade} with {self.percentage} %")
# object - instance of class

Student1 = Student("madhav",13,99)
print(Student1.name)
print(Student1.grade)

Student2 = Student("charu",12,98)
print(Student2.name,Student2.grade) 

Student1.Student_details()
Student2.Student_details()

# oops operation

print(Student1.__dict__)
print(Student2.__dict__)

# modify object property
print(Student1.percentage)# before modifed
Student1.percentage = 100
print(Student1.percentage) # after modified

# Delete object property
print(Student1.__dict__) # before deleted
del Student1.percentage
print(Student1.__dict__) # after deleted



