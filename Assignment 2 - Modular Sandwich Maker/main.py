
import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


def main():

    resources = data.resources
    recipes = data.recipes

    sandwich_maker_instance = SandwichMaker(resources)
    cashier_instance = Cashier()


    sandwich_size = "Medium"
    order_ingredients = {
        "bread": recipes[sandwich_size]["ingredients"]["bread"],
        "ham": recipes[sandwich_size]["ingredients"]["ham"],
        "cheese": recipes[sandwich_size]["ingredients"]["cheese"],
    }
    sandwich_cost = recipes[sandwich_size]["cost"]

    print(f"Please insert coins to pay ${sandwich_cost:.2f}")
    coins_inserted = cashier_instance.process_coins()

    if cashier_instance.transaction_result(coins_inserted, sandwich_cost):
        result = sandwich_maker_instance.make_sandwich(sandwich_size, order_ingredients)
        print(result)
    else:
        print("Transaction failed. Please try again.")


if __name__ == "__main__":
    main()
