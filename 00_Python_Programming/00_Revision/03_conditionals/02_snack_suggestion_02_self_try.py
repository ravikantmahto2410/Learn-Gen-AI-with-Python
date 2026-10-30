## A local cafe wants a Program that suggests a snack.
## If a customer asks for cookies or samosa, it confirms the order.
## Otherwise, it say's not available.

## Task : 
 # Take snack input
 # If it's "Cookies" or "Samosa" , confirm the order
 # Else, Show unavailability


snack = input("Enter Your Order : ").lower()

if snack == "cookies" or snack == "samosa":
    print(f"Your {snack} order is confirmed.")
else:
    print(f"Sorry ! {snack} is unavailable.")