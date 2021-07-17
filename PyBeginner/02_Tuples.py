# About Tuples:

# Once the tuple's content is defined, it becomes immutable (you can't change the already-fixed content).

# How declare a Tuple:
tuple_py = ("Carlos", 20, "M", 600.05)

###################################################################
# tuple_py[2] = "Man"                                            #
#                                                                #
# tuple_py[2] = "Man" # Error in description:                    #
# TypeError: 'tuple' object does not support item assignment     #
##################################################################

print(tuple_py)

print(len(tuple_py)) # return the length of tuple

print(type(tuple_py)) # return the data structure type used

# Other way the declare a Tuple:
tuple_py2 = tuple((10, 15.6, "Mainframe", "C", True, False))

print(tuple_py2)