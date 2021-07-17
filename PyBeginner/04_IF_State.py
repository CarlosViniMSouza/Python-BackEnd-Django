resp = input("Do you want insert number, words, symbols or booleans? : ")
v = input("Input a any value = ")

if resp == "word":
    print(v, " is a string.")
elif resp == "number":
    print(v, " is a integer.")
elif resp == "decimals":
    print(v, " is a float.")
elif resp == "booleans":
    print(v, " is a Boolean")
else:
    print(v, " The type vale isn't identified")

# The python interpreter all the inputs how to strings.
# This code is horrible! LOL