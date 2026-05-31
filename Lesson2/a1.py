# 1) Add the project title.
#    a) Use a comment to label the program as "Recipe Explorer".
print("Recicpe Explorer")
   

# 2) Create tuples for recipe details.
#    a) Store pasta details in a tuple.
#    b) Store biryani details in a tuple.
#    c) Print recipe details using index positions.
Pasta = ("Pasta Arrabiata", "Italian", "20", "Medium")
Biryani = ("Chicken Biryani", "Indian", "45", "Hard")
print(Pasta)
print("name:", Pasta[0])
print("cuisine:", Pasta[1])
print("difficulty:", Pasta[-1])
print("slicing biryani:", Biryani[1:3])
# 3) Use nested tuples and slicing.
#    a) Store both recipe tuples inside one tuple.
#    b) Access details from nested tuples.
#    c) Use slicing to print selected pasta details.
all_recipe = (Pasta, Biryani)
print(all_recipe)
print("first recipe name", all_recipe[0][0])
print("second recipe time", all_recipe[1][2])




# 4) Iterate through a tuple.
#    a) Use a `for` loop to go through each pasta detail.
#    b) Print each detail one by one.
for detail in Pasta:
    print("-", detail)

# 5) Create sets for ingredients.
#    a) Store pasta ingredients in a set.
#    b) Store biryani ingredients in a set.
#    c) Show that duplicate ingredients are not repeated.
#    d) Use `len()` to count ingredients.
pasta_ingredients = {"tomato", "garlic", "olive oil", "chilli", "pasta", "garlic"}

biryani_ingredients = {"rice", "chicken", "garlic", "onion", "tomato", "spices"}
print("pasta ingredients:", pasta_ingredients)
print("biryani ingredients:", biryani_ingredients)
print("Total pasta ingredients:", len(pasta_ingredients))
# 6) Modify a set.
#    a) Use `add()` to add a new ingredient.
#    b) Use `discard()` to remove an ingredient.
pasta_ingredients.add("parmesan")
pasta_ingredients.discard("chilli")
print("\nUpdated pasta ingredients:", pasta_ingredients)
# 7) Perform set operations.
#    a) Use `union()` to combine all ingredients.
#    b) Use `intersection()` to find common ingredients.
#    c) Use `difference()` to find ingredients only in pasta.
#    d) Use `symmetric_difference()` to find ingredients not shared.

all_ingredients = pasta_ingredients.union(biryani_ingredients)
common = pasta_ingredients.intersection(biryani_ingredients)
only_pasta = pasta_ingredients.difference(biryani_ingredients)
unique_to_each = pasta_ingredients.symmetric_difference(biryani_ingredients)
print("\nAll ingredients (union):", all_ingredients)
print("Common ingredients (intersection):", common)
print("Only in Pasta (difference):", only_pasta)
print("Not shared (sym. difference):", unique_to_each)