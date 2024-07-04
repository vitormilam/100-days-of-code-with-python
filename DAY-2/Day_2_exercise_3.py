#Exercise BMI Calculator 3

body_height = float(input("Enter your height: "))
body_weight = int(input("Enter your weight: "))

body_bmi = body_weight / body_height ** 2

print(f"Your BMI is {body_bmi}% of body fat.")

