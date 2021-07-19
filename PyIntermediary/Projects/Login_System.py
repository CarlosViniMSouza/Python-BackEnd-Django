class Login:
    def __init__(self, name, password):
        self.name = name
        self.password = password

name = input('Write your name: ')
password = input('Write your password: ')

print("\nYou doing a Login. Thanks!\n")

class Register:
    def __init__(self, check_name, check_password):
        self.check_name = check_name
        self.check_password = check_password

check_name = input('Write your name again: ')
check_password = input('Write your password again: ')

var1 = Login(name, password)
var2 = Register(check_name, check_password)

if var1.name == var2.check_name and var1.password == var2.check_password:
    print("\nYou're Welcome. Thanks for login in our system")
else:
    print("\nSomething were wrong!")