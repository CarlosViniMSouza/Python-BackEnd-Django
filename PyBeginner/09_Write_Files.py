"""
# Now, let's see how to create, edit and write files via-python.

link = "C:/Users/CarlosViniMSouza/Documents/Programacao/Programacao_Python/python/PyFullCourse/PyBeginner/File-Test.txt"

# first parameter: the address of the file.
# second parameter: the letter characterizes what will be done with the file after its request.
check_file = open(link, "w")

check_file.write("This is a new line text via-file09!")
# here we altered the File-Test.txt

check_file = open(link, "r")
# Now, i want do check the alts doing.

for file in check_file.readlines():
    print(file)
"""
# Now, I'll create a new file:

link_name = "C:/Users/CarlosViniMSouza/Documents/Programacao/Programacao_Python/python/PyFullCourse/PyBeginner/File-Names.txt"

file_names = open(link_name, "w")

file_names.write("Carlos Souza\n")
file_names.write("Antonio Carlos\n")
file_names.write("Pedro Sales")

file_names = open(link_name, "r")
# Now, i want do check the alts doing.

for file in file_names.readlines():
    print(file)
