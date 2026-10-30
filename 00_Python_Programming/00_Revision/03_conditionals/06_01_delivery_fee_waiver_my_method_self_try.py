## You run an online tea store
 # If the order amount is more than RS - 300, delivery is free:
 # Otherwise, it costs Rs - 30


## Task :
# Input :  Order_Amount
# Use Ternary Operator to decide the  delivery fee


order_amount = int(input("Enter your order amount :"))

if order_amount > 300:
    print(f"Order is free")
else:
    print(f"Delivery fee: Rs - 30")