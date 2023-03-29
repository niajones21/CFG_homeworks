class ValueError():
    pass

class CostError():
    pass

stock = {
        "Speaker": 80,
        "Laptop": 150,
        "DVD player": 60
}
def display_items(stock):
    customer_money = 100

    print("Welcome to our store!")
    print("These are our available items and their prices: ")
    for item, price in stock.items():
        print(item, price)

    for i in range(3):
        choice = input("Enter an item to purchase or type 'exit' to leave: ")
        if choice == 'exit':
            print("Thank you for visiting our shop!")
            break

        if choice not in stock:
            print("This item is not available to purchase ")
            raise ValueError("This item is not available to purchase")
        elif stock[choice] <= 100:
            print("Here is your {}".format(choice))
            print("Thank you for shopping with us")
            break
        else:
            print(f"You do not have enough funds to purchase {choice}.")
            has_more_money = input("Do you have any more money? (y/n): ")
        if has_more_money == "y":
                extra_money = int(input("How much extra money do you have?: "))
                new_amount = customer_money + extra_money
                print("Your new balance is {}".format(new_amount))
        else:
            raise CostError("You still don't have enough money. Please leave the shop")


display_items(stock)
