

recipes = {
    "small": {
        "ingredients": {
            "bread": 2, ##slice
            "ham": 4, ##slice
            "cheese": 4, ##ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4, ##slice
            "ham": 6, ##slice
            "cheese": 8, ##ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6, ##slice
            "ham": 8, ##slice
            "cheese": 12, ##ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12, ##slice
    "ham": 18, ##slice
    "cheese": 24, ##ounces
}


class SandwichMachine:

    def __init__(self, machine_resources):
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        for item, amount in ingredients.items():
            if item in self.machine_resources and self.machine_resources[item] < amount:
                print(f"Sorry, there is not enough {item}.")
                return False
        return True

    def process_coins(self):
        large_dollars = int(input("How many large dollars?: "))
        half_dollars = int(input("How many half dollars?: "))
        quarters = int(input("How many quarters?: "))
        nickels = int(input("How many nickels?: "))

        total_value = (
            large_dollars * 1.00 +
            half_dollars * 0.50 +
            quarters * 0.25 +
            nickels * 0.05
        )
        return total_value

    def transaction_result(self, coins, cost):
        if coins >= cost:
            change = coins - cost
            if change > 0:
                print(f"Here is ${change:.2f} in change.")
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        if self.check_resources(order_ingredients):
            cost = recipes[sandwich_size]["cost"]
            print(f"Please insert coins for a {sandwich_size} sandwich (cost: ${cost:.2f}):")
            coins = self.process_coins()
            if self.transaction_result(coins, cost):
                for item, amount in order_ingredients.items():
                    self.machine_resources[item] -= amount
                print(f"{sandwich_size} sandwich is ready. Bon appétit!")


machine = SandwichMachine(resources)

while True:
    user_input = input("What would you like? (small/medium/large/off/report): ").lower()

    if user_input == "off":
        break
    elif user_input == "report":
        for item, amount in machine.machine_resources.items():
            print(f"{item.capitalize()}: {amount} {'slice(s)' if item == 'bread' else 'ounce(s)' if item == 'cheese' else 'slice(s)'}")
    elif user_input in recipes:
        sandwich_size = user_input
        order_ingredients = recipes[sandwich_size]["ingredients"]
        if machine.check_resources(order_ingredients):
            machine.make_sandwich(sandwich_size, order_ingredients)
    else:
        print("Invalid input. Please select a valid option: small, medium, large, off, or report.")
