# Concession stand program

menu = {"pizza": 5.00,
        "nachos": 5.50,
        "popcorn": 5.00,
        "fries": 4.50,
        "chips": 3.00,
        "pretzel": 6.50,
        "soda": 2.00,
        "water": 1.50,
        "candy": 3.50}

cart = []
total = 0

print("---------- MENU ----------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("--------------------------")

while True:
    food = input("Select an item (q to quit): ").lower()

    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("------- YOUR ORDER -------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()

print(f"Total is: ${total:.2f}")