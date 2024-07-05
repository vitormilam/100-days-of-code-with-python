# Is an odd or even number ? 

#Which number do you want to check ?
number_user = int(input("Type a number: "))

# If the number  can be divided by 2 with no remainders:
if number_user % 2:
    print("This is an even number.")
else:
    print("This is an odd number.")
