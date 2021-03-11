number = input("Enter a series of number, using separator you like: ")

separator = ""
for char in number:
    if not char.isnumeric():
        separator = separator + char

print(separator)

sum = 0
for char in number:
    if char not in separator:
      sum = sum + int(char)
       
print(sum)



