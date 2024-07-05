# Roller Coster Tickets 

print("Welcome to the rollercoaster!!")
height = int(input("What's your height? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!!")
    age = int(input("What's your age? "))
    if age <= 7:
        bill = 5
        print("Child tickets are $5 dollars.")

    elif age > 7 and age < 18:
        bill = 7
        print("Youth tickets are $7 dollars.")

    else:
        bill = 12
        print("Adult tickets are $12 dollars.")

    photo = input("Do you want a photo tanken? Y or N: ")
    if photo == "Y" or photo == "y":
        bill += 3
        print(f"Your total with the photo is ${bill} dollars.")

    else: 
        print(f"Your total without the photo is ${bill} dollars.")
else:
    print("Sorry, you have to grow taller before you can ride.")