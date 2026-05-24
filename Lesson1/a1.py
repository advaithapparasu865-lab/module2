# 1) Create a list with a few fruit names:
#    a) Store multiple string items inside a list variable.
fruit = ["banana", "apple", "cherry", "grape"]

# 2) Print basic list details:
#    a) Print the length of the list using `len()`.
#    b) Print the first element using index `[0]`.
#    c) Print the last element using index `[-1]`.
fruit_len = len(fruit)
print(len(fruit)) 
print(fruit[0])
print(fruit[-1])
print(fruit[fruit_len-1])
# 3) Add a new item to the list:
#    a) Use `.append()` to add one more fruit.
#    b) Print the updated list.
fruit.append("orange")
print(fruit)
# 4) Remove an item from the list:
#    a) Use `.remove()` to delete a specific fruit by name.
#    b) Print the updated list.
fruit.remove("cherry")
print(fruit)
# 5) Sort the list:
#    a) Use `.sort()` to arrange items in alphabetical order.
#    b) Print the sorted list.
fruit.sort()
print(fruit)
# 6) Remove an item using index:
#    a) Use `.pop(index)` to remove an element at a specific position.
#    b) Print the updated list.
fruit.pop(0)
print(fruit)
# 7) Reverse the list order:
#    a) Use `.reverse()` to reverse the items.
#    b) Print the reversed list.
fruit.reverse()
print(fruit)
# 8) Multiply the list:
#    a) Print the list repeated multiple times using `list * 2`.
print("multiplication on list", fruit*2)
# 9) Slice the list:
#    a) Keep only the first few elements using slicing (example: `list[:4]`).
#    b) Print the sliced list.
fruit1 = fruit[:2]
print(fruit1)
fruit2 = fruit[1:]
print(fruit2)
# 10) Clear the list:
#     a) Use `.clear()` to remove all elements.
#     b) Print the updated (empty) list.
fruit.clear()
print(fruit)