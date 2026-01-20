# order_amount = int(input("Enter the order amount"))

# print(f"Order amount : {type(order_amount)}")  # here the type is showing us the type of the value that we are getting from the user that is always in str

# To convert the data type from str to int we will write like this


order_amount = int(input("Enter the order amount : "))   # we are using the int here to convert the data type of the value that we are getting
print(f"Order amount : {type(order_amount)}")  # here the type is showing us the type of the value that we are getting from the user that is always in str

# Now lets calculate the delivery fees
delivery_fees = 0 if order_amount > 300 else 30

print(f"Delilvery Fees is : {delivery_fees} ")