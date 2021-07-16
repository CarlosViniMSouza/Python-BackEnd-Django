# About Functions:

# Functions are a kind of 'code bundle' - you code for specific purposes and are only used
# when there is a call during the code compilation process!

# How to create a function:

def printing():
    print("Hello Function")

printing()

# But, in addition, we can declare parameters (variables that will be declared in the function scope):

def ParametersTest(a, b):
    print(a + b)

ParametersTest(5, 10)

# Tip, when calling the function, pass the identification of the parameters. For example:

def client(name, age, gender):
    print(f"The Client {name}, are {str(age)} years old and of gender {gender} requested clinical care.")

client(name = "Carlos Souza", age = 20, gender = "M")

# And, we can insert dates in the function:

def Client(Name, Age, Gender):
    print(f"The Client {Name}, are {str(Age)} years old and of gender {Gender} requested clinical care.")

Name = input("Your name = ")
Age = input("Your age = ")
Gender = input("Your gender = ")

Client(Name, Age, Gender) # The function is working perfectly.

# Continue in the point: 1:35:06