# Quem vai pagar a conta ?
import random

print("WHO IS GONNA PAY THE BIL ?")
friend_1 = input("Best friend name: ")
friend_2 = input("Cousin name: ")
friend_3 = input("Uncle name: ")

list_name = [friend_1, friend_2, friend_3]
list_name_rand = random.randint(0,2)

print(f"{list_name[list_name_rand]} is going to pay the meal today.")