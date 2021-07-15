# About Lists:

countries = ['BRA', 'CHI', 'ARG', 'URU', 'PAR'] # create a list.

print(countries[2]) # return the initials 'ARG'

print(countries[2][1]) # return the word 'R' of word 'ARG'

print(countries[2:]) # return the words: ['ARG', 'URU', 'PAR']

print(countries[1:3]) # return the words: ['CHI', 'ARG']

print(type(countries)) # return: <class 'list'>

countries[0] = 'CAN' # replaces 'BRA' by 'CAN'
print(countries)

print(countries[-1]) # print the last word in the list = PAR

print(countries[-2]) # print the second-last word in the list = URU

var = list(('Carlos', 20, 'M', 100.5)) # using method list() for create a list.

# similar to: var = ['Carlos', 20, 'M', 100.5]

print(var, "\n", type(var))

# Methods List:

var_test1 = list((1, 5, 10))
var_test2 = list(("Pencil", "Book", "Pen"))

var_test1.extend(var_test2) # 1 -> extend() : Add 2 lists in only 1 list.
print(var_test1)

var_test2.append("NoteBook") # 2 -> append() : Add 1 new element in selected list
print(var_test2)