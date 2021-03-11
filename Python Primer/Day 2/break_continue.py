shopping_list = ['milk', 'eggs', 'pasta', 'spam', 'bread', 'rice', 'pasta']

item_to_find = "spam"
found_at = None

for index in range(len(shopping_list)):
    if shopping_list[index] != item_to_find:
        continue
    if shopping_list[index] == item_to_find:
        found_at = index
        break

if found_at != None:
    print("Item found at %d" %found_at)
else:
    print("Item not found anywhere.")