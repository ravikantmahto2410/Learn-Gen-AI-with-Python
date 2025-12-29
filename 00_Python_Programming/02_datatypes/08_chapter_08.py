ingredients = ["water","milk","black_tea"];
print(f" Ingredients are : {ingredients}")
ingredients.append("sugar")    # this append method will add sugar at the end of the this list
print(f" Ingredients after append are : {ingredients}")
ingredients.remove("water")
print(f" Ingredients after remove are : {ingredients}")


### Let's see some more methods 
spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options) #When we want to combine two lists we can do like this
print(f"we have chai ingredients {chai_ingredients}")

############################################
## Now lets see about the insert method
chai_ingredients.insert(2, "black tea");
print(f"we have changed the position of Chai Ingredients {chai_ingredients}")  # In insert method of list we also have to give the idx or position where we want to insert any element

## pop method 
last_added = chai_ingredients.pop()
print(f" The last added ingredient in chai_ingredient is : {last_added}")
print(f"we have poped the last added ingredient from  Chai Ingredients {chai_ingredients}")  # In insert method of list we also have to give the idx or position where we want to insert any element


## reverse method
chai_ingredients.reverse()
print(f"we have reversed  Chai Ingredients {chai_ingredients}")  # In insert method of list we also have to give the idx or position where we want to insert any element

## sort method
chai_ingredients.sort()
print(f"we have sorted  Chai Ingredients {chai_ingredients}")  # In insert method of list we also have to give the idx or position where we want to insert any element

## max() and min() methods
sugar_levels = [1, 2, 3, 4, 5]
print(f"Maximum in sugar_levels list : {max(sugar_levels)}")  # In insert method of list we also have to give the idx or position where we want to insert any element
print(f"Minimum in sugar_levels list : {min(sugar_levels)}")  # In insert method of list we also have to give the idx or position where we want to insert any element


####  Operator Overloading    # date - 29_dec

base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]

full_liquid_mix = base_liquid + extra_flavor   ## this is known as the operator Overlaoding
print(f"liquid mix : {full_liquid_mix}" )


strong_brew = ["Black tea"] * 3
print(f"Strong brew : {strong_brew}")


strong_brew_02 = ["Black tea", "Water"] * 3
print(f"Strong_brew part-02 : {strong_brew_02}")


## Suppose we want to we have a string “CINNAMON” and we want to convert this string into the list
## to do this we do like this

raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
print(f"Bytes : {raw_spice_data}")



