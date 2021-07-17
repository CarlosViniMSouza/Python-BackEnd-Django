"""
'Dictionaries' is a Data Structure, where we do use of concept 'key' : 'value' -> in other words, use dicts
for attribute something in something. Example:

"Apple" : 1,
"Banana" : 2,
"Orange" : 3,
...
Ok, let's go to our Lesson:

NOTE: Once the 'key: value' relation is made, the interpreter will ignore any attempts to interfere
with changing the keys.
"""

dict_person = {
    "name": "Carlos Souza",
    "age": 20,
    "gender": "M",
    "college": "Software Engineering",
    "studying": True,
    "friends": ['Adam', 'Rafael', 'Vinicius']
}

print(dict_person) # printed the content of dict
# output : {'name': 'Carlos Souza', 'age': 20, 'gender': 'M', 'college': 'Software Engineering', 'studying': True,
# 'friends': ['Adam', 'Rafael', 'Vinicius']}

print(len(dict_person)) # printed the quant. 'key: value' exist
# output : 6

print(type(dict_person))
# output : <class 'dict'>

print(dict_person["college"]) # accessing a value of dict
# output : Software Engineering

var = dict_person["name"] # can attribute a value in a variable independent.
print(var)
# output : Carlos Souza