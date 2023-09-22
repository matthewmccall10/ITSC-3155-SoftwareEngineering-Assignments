
class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))

        total_amount = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
        return total_amount

    def transaction_result(self, coins, cost):
        if coins >= cost:
            change = coins - cost
            print(f"Here is your change: ${change:.2f}")
            return True
        else:
            print("Sorry, the payment is insufficient.")
            return False
