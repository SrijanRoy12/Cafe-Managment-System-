menu = {
    'pizza': 40,
    'pasta': 50,
    'burger': 60,
    'salad': 70,
    'coffee': 80,
}

# greet
print("welcome to our restaurant")
print("pizza: Rs 40\nPasta: Rs 50\nBurger: Rs 60\nSalad: Rs 70\nCoffee: Rs 80")

order_total = 0

while True:
    item = input("Enter the name of the item you want to order =")
    if item in menu:
        quantity = int(input(f"Enter the quantity of {item} you want to order ="))
        order_total += menu[item] * quantity  # calculate total cost for item
        print(f"Your item {item} has been added to your order")
    else:
        print(f"order item {item} is not available yet ! ")

    another_order = input("Do you want to add another item?(yes/no)")
    if another_order.lower() != "yes":
        break

print(f"the total amount of items to pay is {order_total}")

# ask for dine in or take away
dine_in = input("Will you be dining in or taking away?(dine in/take away) =")

if dine_in.lower() == "dine in":
    # print message for dine in
    print("Please wait while we prepare your order.")
    # ask for mineral water
    mineral_water = input("Would you like to have mineral water?(yes/no) =")
    if mineral_water.lower() == "yes":
        print("Mineral water has been added to your order.")
        order_total += 20  # assume mineral water costs Rs 20
    else:
        print("No mineral water will be provided.")
    # generate QR code for payment
    print("Here is your QR code for payment:")
    # code for generating QR code
    # ...
    # assign seat number
    seat_number = "123"
    print(f"Your seat number is {seat_number}. Please proceed to your table.")
else:
    # print message for take away
    print("Please wait while we prepare your order for take away.")
    # ask for mineral water
    mineral_water = input("Would you like to have mineral water?(yes/no) =")
    if mineral_water.lower() == "yes":
        print("Mineral water has been added to your order.")
        order_total += 20  # assume mineral water costs Rs 20
    else:
        print("No mineral water will be provided.")
    # generate QR code for payment
    print("Here is your QR code for payment:")
    # code for generating QR code
    # ...

# payment options
print("Please select a payment option:")
print("1. Cash")
print("2. UPI")
print("3. Credit/Debit Card")

payment_option = input("Enter your payment option (1/2/3) =")

if payment_option == "1":
    print("You have chosen to pay with Cash.")
    print("Please pay the amount at the counter.")
elif payment_option == "2":
    print("You have chosen to pay with UPI.")
    upi_id = input("Enter your UPI ID =")
    print(f"Payment of Rs {order_total} has been initiated to {upi_id}.")
elif payment_option == "3":
    print("You have chosen to pay with Credit/Debit Card.")
    card_number = input("Enter your Card Number =")
    print(f"Payment of Rs {order_total} has been initiated to Card Number {card_number}.")
else:
    print("Invalid payment option. Please try again.")

# goodbye message
print("Thank you for dining with us!")
print("Please visit again soon!")
