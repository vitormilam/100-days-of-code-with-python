#Exercise BMI Calculator 3

body_height = float(input("Enter your height: "))
body_weight = int(input("Enter your weight: "))

body_bmi = body_weight / body_height ** 2

print(f"Your BMI is {body_bmi}% of body fat.")

if body_bmi < 18.5:
    print("You are underweight.")

elif body_bmi >= 18.5 and body_bmi < 25:
    print("You have a normal weight.")

elif body_bmi >= 25 and body_bmi < 30:
    print("You are slightly overweight.")
    
elif body_bmi >= 30 and body_bmi < 35:
    print("You are obese.")
else:
    print("You are clinically obese.")
