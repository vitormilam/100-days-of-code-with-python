#Exercise Tip Calculator

print("Welcome to the Tip Calculator!")

bill_total = float(input("What was the total bill? $"))
tip_porcentage = float(input("How much tip would you like to give ? 10, 12 or 15 ? "))
bill_people = int(input("How many people to split the bill ? "))

#Calculate the tip amount:
tip_amount = bill_total * (tip_porcentage / 100)

#Calculate the amount each person should pay:
bill_value_per_person = bill_total / bill_people

# Format the result to 2 decimal places
bill_value_per_person = int(bill_value_per_person)

print(f"Each person should pay ${bill_value_per_person} dollars.")