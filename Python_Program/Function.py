#in Python function is group of related statments that perform a specific task.
#function declaration
def GreetMe():  #function start with def and after name of that function.
    print("Good Morning")   #code

GreetMe()   #call fucntion.

print("------------  New Function  ------------------")
#sand peramiter in the function.
def morning(name):
    print("Good Morning"+name)

morning(" Prins")   #prins sand to function(morning) peramiter(name) and print usint + operator.
print("------------  New Function  ------------------")
#function use to sum of 2 values
def total(a,b): #peramiter use to store value
    print(a+b) #sum of two value
#call the function
total(2,3) #pass value for sum

print("------------  New Function  ------------------")

#return function
def tot(a, b):
    return a+b #using return store value
#call function and print
print(tot(7,3))