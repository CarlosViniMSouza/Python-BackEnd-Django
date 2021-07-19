"""
Python is a language objects oriented. Well, so it's means that classes, objects, and things like that,
were classified as objects oriented. Classes is like a constructors in Python, a type of function.
"""

class Login:
    def __init__(self, name, password):
        self.name = name
        self.password = password

name = input('Write your name: ')
password = input('Write your password: ')

user = Login(name, password)

print("Your Login is:\n", user.name, "\n", user.password)

"""
What happened: We created a class called 'Login', which has the function parameters below (name and password) 
as properties. When the 'user' variable received the 'Login class', it also received its properties.
"""

# Now, if have a class empty, use the keyword pass (she permit the code execute the orders in sequence).

class Empty:
    pass

var = Empty()
print(var) # <__main__.Empty object at 0x000001C0E01E2CD0>

var2 = Empty
print(var2) # <class '__main__.Empty'>