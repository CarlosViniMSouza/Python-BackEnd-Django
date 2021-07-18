# At times, it may be necessary to read text files, html format, and other extensions.
# For that, we'll look at some python keywords to fix this problem.

link = "C:/Users/CarlosViniMSouza/Documents/Programacao/Programacao_Python/python/PyFullCourse/PyBeginner/File-Test.txt"

# first parameter: the address of the file.
# second parameter: the letter characterizes what will be done with the file after its request.
check_file = open(link, "r")

# print(check_file.readlines()) --> # here the program will printer the text in format list.

for file in check_file.readlines():
    print(file)

check_file.close()