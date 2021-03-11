age = int(input("How old are you ?"))
print(type(age))

if 18 <= age <= 25:
    print("You are an early adult")
elif age >25:
    print("You are now legit adult")
else:
    print("You are such a kiddo...")