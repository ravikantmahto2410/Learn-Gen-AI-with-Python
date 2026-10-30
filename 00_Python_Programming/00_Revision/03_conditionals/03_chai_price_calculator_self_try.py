## problem Statement :
## A Tea Stall Offers different  prices for different cup sizes.
## Write a Program that calculates the price based on size

## Task : 
  # Input : "small", "medium", "large"
  # Small -> 10, Medium -> 15, Large -> 20
  # If Invalid : show "Unknown cup size"

cup_size = input("Enter the Tea Cup Size : ").lower()

if cup_size == "small":
    print(f"Price for {cup_size} is Rs - 10")
elif cup_size == "medium":
    print(f"Price for {cup_size} is Rs - 15")
elif cup_size == "large":
    print(f"Price for {cup_size} is Rs - 20")
else:
    print(f"Invalid cup size")