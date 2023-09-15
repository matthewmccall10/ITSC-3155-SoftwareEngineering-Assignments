class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, order_ingredients):
        for ingredient, quantity in order_ingredients.items():
            if ingredient in self.machine_resources and self.machine_resources[ingredient] < quantity:
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        if self.check_resources(order_ingredients):
            # Deduct the used ingredients from machine resources
            for ingredient, quantity in order_ingredients.items():
                self.machine_resources[ingredient] -= quantity
            return f"Here is your {sandwich_size} sandwich. Enjoy!"
        else:
            return "Sorry, we don't have enough ingredients to make your sandwich."