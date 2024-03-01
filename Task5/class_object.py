class Student: 
    def __init__(self, name, age, institute, departement, ID ):
        self.name = name 
        self.age = age 
        self.institute = institute
        self.department  = departement
        self.ID = ID 
    def showMe(self):
        print(f"\nMy name is {self.name}. \nI'm {self.age} years old. \nI'm studying in {self.institute} department of {self.department}. \nMy student ID is {self.ID}!!\n") 
        
        
s1 = Student("Md. Sultan Mahmud", 20, "RU", "Statistics", "2110924122")
# print(s1.name)
s1.showMe()