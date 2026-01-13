chai_order = dict(type="Masala Chai", size="Large", sugar=2)  ## this is dictionary list
print(f"Chai Order : {chai_order}")

## above this line This is just brief overview of dict

#####################################################################################################

## Now lets see how we can add the data , how we can remove the data

# First see how can we add the data
chai_recipe = {} ## We can create the dictionary like this also
chai_recipe["base"] = "black tea" # here base is the and the "black tea" is the value
chai_recipe["liquid"] = "milk"

print(f"Recipe base : {chai_recipe['base']}")

######################################################################################
# lets see now how we can remove or delete the elments 

print(f"Recipe: {chai_recipe}")
del chai_recipe ["liquid"]
print(f"Recipe : {chai_recipe}")

###############################################################################
# now lets check about he membershp , because almost everywhere we have list , be it in square brackets, curly braces and set , we can do the membership test
print(f"Is sugar in the order ? {'sugar' in chai_order}")

chai_order = dict(type="Ginger Chai", size="Medium", sugar=1)  ## Here we have redefined the dictionary
# print(f"Order details (keys) : {chai_order.keys()}") ## Since the keys is a method we have to put the parenthesis, and what do we mean by the keys are : , "type" is key, "size" is a key, "sugar" is a key 
# print(f"Order details (values) : {chai_order.values()}")
# print(f"Order Details (items) : {chai_order.items()}")

last_item = chai_order.popitem() # popitem just remove the item
print(f"Removed last item : {last_item}")

extra_spices = {"cardamom" : "crushed", "ginger":"sliced"}
chai_recipe.update(extra_spices)
print(f"Updated Chai Recipe : {chai_recipe}")

## now lets see what happens when we try to get the things which is not present in the list ,method used in  line 41   will give  the error 
# chai_size = chai_order["customer_note"] this  way it will give the error when we try to get the "customer_note"
chai_size = chai_order.get("size", "NO Note") # if we dont get the "note"  we will mark it with the "No Note" was given by the customer
print(f"Chai size is : {chai_size}")




