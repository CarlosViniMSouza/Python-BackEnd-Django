# I'll start this project tomorrow.
cond = "y"

while cond == "Y" or cond == "y":

    n1 = float(input("Write a number: "))

    print("Operators: \n+ (sum) \n- (minus) \nx (product) \n/ (div)")
    print("^ (expo) \nsqrt (square root) \nmod (modulus div)")

    op = input("Write the operator: ")
    n2 = float(input("Write a number: "))

    if op == "+":
        print("Your resp is = ", n1 + n2)
    elif op == "-":
        print("Your resp is = ", n1 - n2)
    elif op == "x":
        print("Your resp is = ", n1 * n2)
    elif op == "/":
        print("Your resp is = ", n1 / n2)
    elif op == "^":
        print("Your resp is = ", n1 ** n2)
    elif op == "sqrt":
        print("Your resp is = ", n1 ** 0.5)
    elif op == "mod":
        print("Your resp is = ", n1 % n2)
    else:
        print("Operation Impossible. Try again!")
    resp = input("Do you want continue? [Y] or any letter: ")
    cond = resp

# Continuation in 2:45:36