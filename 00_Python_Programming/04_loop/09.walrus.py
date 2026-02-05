##### Section - 1 : This is section is without using walrus operator

# value = 13
# remainder = value % 5

# if remainder:
#     print(f"Not Divisible, remainder is {remainder}")


### Now lets see how can we write the exact code of section -1 using the walrus operator
## Using the walrus operator
value = 13

if(remainder := value % 5):
    print(f"Not Divisible, remainder is {remainder}")


##### Lets see another example
available_sizes = ["small", "medium", "large"]
if(requested_size := input("Enter your chai cup size: ")) in available_sizes:
    print(f"Serving {requested_size} chai")
else:
    print(f"{requested_size} is unavailable")


### another example
flavors=["masala", "ginger", "lemon", "mint"]

print("Available flavors:", flavors)

while(flavor := input("Choose yoour flavor: ")) not in flavors:
    print(f"Sorry, {flavor} is not available")

print(f"You choose {flavor} chai")
