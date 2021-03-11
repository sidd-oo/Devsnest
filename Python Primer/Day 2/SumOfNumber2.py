number = input("Enter a series of number, using separator you like: ")

separator = ""
for char in number:
    if not char.isnumeric():
        separator = separator + char

print(separator)

str = 0;
sum = 0
for char in number:
    if char not in separator:
        str = str * 10 + int(char)
        if char == number[len(number)-1]:
            sum = sum + int(char)
    elif char in separator:
        sum = sum + str 
        str = 0

print(sum)




