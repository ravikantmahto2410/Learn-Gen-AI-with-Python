# ideal_temp = 95.5
# current_temp = 95.4999999999


##Example- 2.15.12 : In the above example the value that we are getting for Difference temp is something that we didn't expected, If we take lesser precision in  current_temp, it will behave differently


ideal_temp = 95.5
current_temp = 95.49
print(f"Ideal temp {ideal_temp}")
print(f"Current temp { current_temp }")
print(f"Difference temp {ideal_temp - current_temp}")

