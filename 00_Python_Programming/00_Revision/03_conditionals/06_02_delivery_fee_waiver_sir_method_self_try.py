## You run an online tea store
 # If the order amount is more than RS - 300, delivery is free:
 # Otherwise, it costs Rs - 30


## Task :
# Input :  Order_Amount
# Use Ternary Operator to decide the  delivery fee


order_amount = int(input("Enter the Order_Amount : "))

delivery_fees = 0 if order_amount > 300 else 30

print(f"Delivery fees is {delivery_fees}")











