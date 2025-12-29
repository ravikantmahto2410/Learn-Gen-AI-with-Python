masala_spices = ("cardamom", "cloves", "cinnamon")  ### tuples() are immutable that means they can't be changed

### Sometimes we already have tuples and ,so we just have to extract or unpack the values out of it  , to do that we do like this
(spice1, spice2, spice3) =  masala_spices
print(f"Main masala spices : {spice1}, {spice2}, {spice3}")

### we can also assign the values to the variables like this
ginger_ratio ,cardamom_ratio  = 2, 1 ## by writing like this , the 2 will be allocated to ginger_ratio and the 1 will be allocated to the cardamom_ratio
print(f"Ratio of Ginger and Cardamom  = {ginger_ratio} : {cardamom_ratio}")

## In Python we can also swap the values of these two variables ginger_ratio and cardamom_ratio like this
ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio
print(f"Ratio of Ginger and Cardamom  = {ginger_ratio} : {cardamom_ratio}")


## Now lets see about the membership test
print(f"Is Ginger present in masala_spices ? {'ginger' in masala_spices}") ## WE are checking whether the ginger is present in masala_spices = ("cardamom", "cloves", "cinnamon")
print(f"Is cinnamon present in masala_spices ? {'cinnamon' in masala_spices}") ## WE are checking whether the cinnamon is present in masala_spices = ("cardamom", "cloves", "cinnamon")
print(f"Is Cinnamon present in masala_spices ? {'Cinnamon' in masala_spices}") ## WE are checking whether the Cinnamon is present in masala_spices = ("cardamom", "cloves", "cinnamon")

































