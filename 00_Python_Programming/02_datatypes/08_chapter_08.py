ingredients = ["water","milk","black_tea"];
print(f" Ingredients are : {ingredients}")
ingredients.append("sugar")    # this append method will add sugar at the end of the this list
print(f" Ingredients after append are : {ingredients}")
ingredients.remove("water")
print(f" Ingredients after remove are : {ingredients}")


## Let's see some more methods 
spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options) #When we want to combine two lists we can do like this
print(f"we have chai ingredients {chai_ingredients}")

###########################################
# Now lets see about the insert method
chai_ingredients.insert(2, "black tea");
print(f"we have changed the position of Chai Ingredients {chai_ingredients}")  # In insert method of list we also have to give the idx or position where we want to insert any element

# pop method 
last_added = chai_ingredients.pop()
print(f" The last added ingredient in chai_ingredient is : {last_added}")
print(f"we have poped the last added ingredient from  Chai Ingredients {chai_ingredients}")  # In insert method of list we also have to give the idx or position where we want to insert any element


# reverse method
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





####################################################################
# My Own revision or Investigative STudy
my_car_list = ["Range Rover", "Tata Safari", "Tata Harrier", "Tata Sierra"];
print(f" My Car list Includes : {my_car_list}")
my_car_list.append("Harrier.ev")    # this append method will add sugar at the end of the this list
print(f" My Cars after append : {my_car_list}")
print(f"ID of my_car_list  : {id(my_car_list)}")
my_car_list.remove("Tata Safari")
print(f" My Cars after  after remove are : {my_car_list}")
print(f"ID of my_car_list  : {id(my_car_list)}")


## no Lets Revise the  extend method
my_ev_car_list = ["Harrier.ev", "Curvv.ev", "Nexon.ev", ]
my_fuel_cars = ["Range Rover", "Tata Harrier", "Tata Safari"]
my_ev_car_list.extend(my_fuel_cars);
print(f"My all cars are : {my_ev_car_list}")


##### Revision
#### Revision 2nd time date - 14/08/2026

mycars = ['harrier', 'fortuner', 'safari'];
print(f'my cars are : {mycars}')

mycars.append("curvv")
print(f'mycars after append : {mycars}')
mycars.append(['Bullet 350','Hunter'])
print(f'mycars after append CDT : {mycars}')

mycars.append(0)
print(f'mycars appended : {mycars}')

mycars.append({'GLA','GLS', 'GLC'})
print(f'my cars appended again : {mycars}')

mycars.append(('Grand Vitara', 'Scorpio', 'XUV700'))
print(f'mycars appended again {mycars}')


### remove method
mycars.remove(['Bullet 350', 'Hunter'])
print(f'mycars should not have bike:{mycars}')

mycars.remove(0)
print(f'my cars should have no numbers {mycars}')

mycars.remove({'GLS','GLA','GLC'})
print(f'mycars list should not have costly cars {mycars}')

mycars.remove(('Grand Vitara', 'Scorpio', 'XUV700'))
print(f'mycar list remove these vehicles:{mycars}')


### extend methods

tatacars = ['Harrier', 'Safari', 'Curvv']
toyotacars = ['Fortuner', 'Innova', 'Glanza']

tatacars.extend(toyotacars)
print(f'toyota cars mixed into : {tatacars}')
tatacars.extend('Nexon')
print(f'can we print  {tatacars}')

tatacars.extend({'tiago','Tigor'})
print(f'more tata cars:{tatacars}')

tatacars.extend(('Sierra'))
print(f'one more card added : {tatacars}')
tatacars.extend(('Punch',))
print(f'more tata cars added : {tatacars}')

### insert method
## syntax : 