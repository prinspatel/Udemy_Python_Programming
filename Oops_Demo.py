#classes are nothing but define blueprint protocol
class Calculator:
    num = 100 #class variable
    #default constructor
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print("I am called automatically when object is created")

    def getData(self):
        print("I am now executing as method in Class")

    def Summation(self):
        return self.a + self.b + self.num

obj = Calculator(2,3) #Syntex to crate object
obj.getData()
print(obj.Summation()) #class class object

obj2 = Calculator(10, 5)
print(obj2.Summation())
