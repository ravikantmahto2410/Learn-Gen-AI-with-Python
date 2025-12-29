is_boiling = True
stri_count = 5
total_actions = stri_count + is_boiling ## this is upcasting
print(f"Total actions : {total_actions}")

## Lets see one more interesting thing

milk_present = 0 # no milk
print(f"Is there milk : {bool(milk_present)}")  ### Here bool() is a function or method and since we know that anthing that is function it has two Parenthesis , Here milk_present is getting converted into the bool

# another example  to understand the interesting thing
water_present = 11
print(f"Is water Present : {bool(water_present)}")

## lets see using None
water_present2 = None
print(f"Is water2 Present : {bool(water_present2)}")


## Now lets see Logical Operations that is 1.) AND, 2.) OR , 3.) NOT

# First lets see the AND
water_hot = True
tea_added = True

can_server = water_hot and tea_added
print(f"Can I serve Chai ? {can_server}")