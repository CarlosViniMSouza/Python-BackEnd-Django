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

var_test2.append("NoteBook") # 2 -> append() : Add 1 new element in selected list.
print(var_test2)

print(len(var_test1)) # 3 -> len() : return the length of list.

var_test2.insert(1, "PDFs") # 4 -> extend() : Add 1 new object in the position that you chose.
print(var_test2) # -> In this case, the element "PDFs" was add in position var_test2[1].

var_test1.remove(5) # 5 -> remove() : Remove 1 element selected of list.
print(var_test1)

var_test2.clear() # 6 -> clear() : remove all elements of list.
print(var_test2)

print(var_test1.index('Book')) # 7 -> index() : return the position of element in list.

var_test3 = [1, 10, 5, 20, 15, 30] # a new list called var_test3.

var_test3.sort() # 8 -> sort() : rearranges elements in descending order.
print(var_test3)

var_test3.reverse() # 9 -> reverse() : invert the list.
print(var_test3)

var_test3.pop(2) # 10 -> pop() : delete a element in the position specific
# similar to: del var_test3[2]

print(var_test3)

# In next session: Tuples in python!