#Restorent project 

menu = {
    "pizza" : 120,
    "burger" : 60,
    "pasta" : 80,
    "coffee": 70,
    "tea": 40,
    "Juice": 50
    }
total_order = 0

print("Welcome to our Python Resto")
print(" Pizza: $10\n Buger: $6\n Paasta: $7\n Coffee: $5\n Tea: $3\n Juice: $4")
item1 = input("Enter the item name you want to enter: ").lower()

while True:
    if item1 in menu:
        total_order += menu[item1]
        print(f"Your order {item1} has been added in your order")

    else:
        print(f"You ordered {item1} isn't available yet ")

    another_order = input("Do you want to order an other item ? (Yes/NO): ").lower()
    if another_order == 'yes':
        item2 = input("Enter the name of second order: ")
    elif another_order == "no":
        print("Thank you for contact us.")
        break
    if item2 in menu:
        total_order += menu[item2]
        print(f"your second order {item2} has been add to your order")
    else:
        print(f"Your order {item2} isn't available yet")
print(f"You ordered {item1} and {item2}")
print("The total amout of items you buy is: ",total_order)