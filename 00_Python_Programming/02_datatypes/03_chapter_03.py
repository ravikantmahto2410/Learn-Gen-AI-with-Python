black_tea_grams = 14
ginger_grams = 3

total_grams = black_tea_grams + ginger_grams
print(f"Total grams of base tea is  {total_grams}")

remaining_tea = black_tea_grams - ginger_grams
print(f"Total grams of remaining tea is  {total_grams}")


## Division is little bit complex int the python
# Lets see
milk_litres = 7
servings = 4
milk_per_serving = milk_litres / servings
print(f"Milk per serving is {milk_per_serving}")
#### Example - 2.15.01 
#################################################################################

## Sometimes we don't want to be as exact that we are getting in Example - 2.15.01
total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots
print(f"Whole tea bags per pot : {bags_per_pot}")
#Example - 2.15.02

##########################################################
#### to find the remainder of the diviion operator , we use modulo (%) operator
total_cadamom_pods = 10
pods_per_cup = 3
leftover_pods = total_cadamom_pods % pods_per_cup
print(f"Leftover C pods {leftover_pods}")

#Example - 2.15.03

##############################################################
## now lets see how scale works
base_flavor_strength = 2
scale_factor = 3
powerful_flavour = base_flavor_strength ** scale_factor
print(f"Scaled flavour strength {powerful_flavour}")

## what this actually does is power of two like 2 * 2 * 2
##Example- 2.15.04

##############################################################
##to improve the the code readability , we can write the billion or millions like this billion = 1_000_000_000 ,
# and the python willl treat this as 1000000000
total_tea_leaves_harvested = 1_000_000_000
print(f"Tea leaves : {total_tea_leaves_harvested}")

#Example- 2.15.05












