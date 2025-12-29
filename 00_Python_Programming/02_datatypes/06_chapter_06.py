chai_type = "Ginger chai"
customer_name = "Priya"

print(f"Order for {customer_name} : {chai_type} Please!")

#  Now Lets understand about the indexing 

# chai_description = "Aromatic and Bold"
# print(f"First Word : {chai_description[0:7]}")  # In this range the chai_description[0:7]  here the 7 is exclusive 

# ### Example - 2.16.03 just above

# chai_description = "Aromatic and Bold"
# print(f"First Word : {chai_description[0:8]}")  # In this range the chai_description[0:7]  here the 7 is exclusive 
### Example - 2.16.04 just above

###### Lets see One more interesting thing
chai_description = "Aromatic and Bold"
print(f"First Word : {chai_description[0:8:1]}") ### In this chai_description[0:8:1] here 1 means the pick every next character 

# Example - 2.16.05

chai_description = "Aromatic and Bold"
print(f"Every Second  Word : {chai_description[0:8:2]}") ### In this chai_description[0:8:2] here 1 means the pick every second character 

# Example - 2.16.06  Just above

#  ## Some Pythonic Stuffs
print(f"First  Word : {chai_description[:8]}") ### In this chai_description if we give like[:8] this way we can use when we want to start from the 0th but we can't skip the pythonic column
print(f"Last  Word : {chai_description[12:]}") ### In this chai_description here if we give like[12:] this way we can  get the last word , if we dont mention the last number after colon , then it means take all whatever it takes
print(f"Revered  Word : {chai_description[::-1]}") ### In this chai_description here if we give like[::-1] this way we can  get the revered word , 


### Sometimes we will not be dealing with the only the english , sometimes we will be dealing with the special symbols and other languages like spanish , Japanese and all , for that we need to encode

label_text = "Chai Spécial"
ecoded_label = label_text.encode("utf-8")
print(f"Non Encoded label : {label_text}")
print(f"Encoded label : {ecoded_label}")
decoded_label = ecoded_label.decode("utf-8")
print(f"Decoded label : {decoded_label}")





