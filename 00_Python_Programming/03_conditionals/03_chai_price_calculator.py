## problem Statement :
## A Tea Stall Offers different  prices for different cup sizes.
## Write a Program that calculates the price based on size

## Task : 
  # Input : "small", "medium", "large"
  # Small -> 10, Medium -> 15, Large -> 20
  # If Invalid : show "Unknown cup size"

cup_size = input("Choose your cup size (small/ medium/large) : ").lower()

if cup_size == "small":
    print("Price is 10 rupees")
elif cup_size == "medium":
    print("Price is 15 rupees")
elif cup_size == "large":
    print("Price is 20 rupees") 
else:
    print("Unknown cup size")   






