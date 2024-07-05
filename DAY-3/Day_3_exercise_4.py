#Exercise Automatic pizza ordem program

print("Thank you for choosing Python Pizza Deliveries!!")
size = input("What size pizza do you want ? S, M or L: ").lower()
add_pepperoni = input("Do you want Pepperoni? Y or N: ").lower()
extra_cheese = input("Do you want extra cheese? Y or N: ").lower()

# Pizza Bill
bill = 0
if size == "S":
    bill += 15

elif size == "M":
    bill += 20

else:
    bill += 25

# Pepperoni Bill
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# Cheese Bill
if extra_cheese == "Y":
    bill += 1

# Final Price
print(f"Your final bill is ${bill}.")
