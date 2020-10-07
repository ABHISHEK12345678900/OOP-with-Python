# Defining the class
class Students:
    # Constructor
    def __init__(self, name, usn, age):
        self.Name = name
        self.Usn = usn
        self.Age = age
        print("My name is : {}, My Usn is : {} and My age is : {}".format(self.Name, self.Usn, self.Age))

# Creating the objects "OR" instantiation
abhishek = Students('Abhi', 700, 23)
lohit = Students('Lohit', 31, 23)
chetan = Students('Chetan', 111, 23)
# kartik = Students()