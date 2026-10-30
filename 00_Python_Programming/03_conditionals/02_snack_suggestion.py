## A local cafe wants a Program that suggests a snack.
## If a customer asks for cookies or samosa, it confirms the order.
## Otherwise, it say's not available.

## Task : 
 # Take snack input
 # If it's "Cookies" or "Samosa" , confirm the order
 # Else, Show unavailability




snack = input("Enter your preferred snack: ").lower()

if snack == "cookies" or snack == "samosa":
    print(f"Great Choice! We'll serve you {snack}")

else:
    print(f"Sorry we only serve cookies and Samosa with tea")    