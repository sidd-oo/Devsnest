print("Hello World")
print('"This is a quote...blah blah"')

greetings = "Hello"
name = input("Please enter your name:");
print(greetings + ", "+ name)

# Escape Characters
print("Hey there, \" Bring me some food\" ")
print('\n')

#Splitting over serveral lines
anotherString = """This string
is splitted into
serveral lines.
"""

print(anotherString)

# 
firstName = "Vaibhav"
secondName = "Mahajan"
print(firstName + secondName);
print("Vai" in firstName);


# Formatting of Strings

for i in range(1, 13):
    print("No. {0:1} squared is {1:3} and cube is {2:4}".format(i, i**2, i**3))


# f string and other formatting ways

name = "Subashish"
age = 47
print(name + f" is according to {age}");
print(name + " is accordign to {0}".format(age))
print(name + " is %s years old" %age)

