# Love Score
# Functions lower(), count()

print("The love calculator is calculating your score...")
name_1 = input("What's your name? ").lower()
name_2 = input("What's their name? ").lower()
combined_names = name_1 + name_2

# Matching true
t = combined_names.count("t")
r = combined_names.count("r")
u = combined_names.count("u")
e = combined_names.count("e")
first_digit = t + r + u + e

# Matching love
l = combined_names.count("l")
o = combined_names.count("o")
v = combined_names.count("v")
e = combined_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")

elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")