"""
Try Except -> The idea is prevent errors in execution of program. He will interrupter the process
when the code crusher in a moment of compilation code. Example:
"""
"""
try:
    n = int(input('Insert a number: '))
    print(n)
except:
    print('invalid data.')
    # if you input a float, a char, a boolean or a string,
    # the program will show message 'invalid data'
"""

# if we need to specify the input data type, we can use the 'ValueError' method:
"""
try:
    num = float(input('Insert a number decimal = '))
    print("Your number is: ", num)
except ValueError:
    print('Error in Data Type.')
"""
# In addition, it reports an error in the use and control of variables.

# And if necessary, we can add the 'else' conditional structure:
"""
try:
    num = float(input('Insert your number = '))
    print("Your number is: ", num)
except:
    print('Error in Data Type.')
else:
    print("All right! You can continue.")
"""

# 'Finally' is also a keyword. Now this is going to run either there
# is an error or not. So i can just say: "try accept, finished."
try:
    num = float(input('Insert a number decimal = '))
    print("Your number is: ", num)
except:
    print('Error in Data Type.')
finally:
    print('try except finished.')
