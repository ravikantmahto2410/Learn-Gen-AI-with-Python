essential_spices = {"cardamom", "ginger","cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

all_spices = essential_spices | optional_spices  ## this will give us the union of both essential_spices and optional_spices
print(f"All Spices are : {all_spices}")

common_spices = essential_spices & optional_spices   # this will find the common among the set  essential_spices and the optional_spices
print(f"Common spices are : {common_spices}")

## Difference of :  Now lets see how to find the elements which are present in one but not present in the other set  : t
only_in_essential = essential_spices - optional_spices
print(f"Spices  only in essential_spices are : {only_in_essential}")

## Membership test
print(f"Is 'Cloves'  in essential spices? {'cloves' in essential_spices}")
print(f"Is 'Cloves'  in Optional spices? {'cloves' in optional_spices}")










