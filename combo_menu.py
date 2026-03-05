flavor = input("What ice cream flavor would you like? Vanilla ($3.00), Chocolate ($3.25), or Strawberry ($3.50)? ")
total_cost = 0.00
flavors = ["vanilla", "chocolate", "strawberry"]
flavor = flavor.lower()
while flavor not in flavors:
    flavor = input("Please enter Vanilla, Chocolate, or Strawberry: ").lower()
if flavor == "vanilla":
    total_cost = 3.00
elif flavor == "chocolate":
    total_cost = 3.25
elif flavor == "strawberry":
    total_cost = 3.50
YesorNoToppings = input("Would you like toppings? ")
YesorNoToppings = YesorNoToppings.lower()
ToppingsList = ["yes", "no"]
while YesorNoToppings not in ToppingsList:
    YesorNoToppings = input("Please enter yes or no: ").lower()
if YesorNoToppings == "yes":
    ToppingSize = input("What size topping portion would you like? Small ($0.50), Medium ($0.75), or Large ($1.00)? ")
    ToppingSize = ToppingSize.lower()
    ToppingSizes = ["small", "medium", "large"]
    while ToppingSize not in ToppingSizes:
        ToppingSize = input("Please enter small, medium, or large: ").lower()
    if ToppingSize == "small":
        total_cost += 0.50
        MegaSize = input("Would you like to mega size your toppings for an extra $0.50? ")
        MegaSize = MegaSize.lower()
        while MegaSize not in ["yes", "no"]:
            MegaSize = input("Please enter yes or no: ").lower()
        if MegaSize == "yes":
            total_cost += 0.50
            ToppingSize = "large"
        elif MegaSize == "no":
            ToppingSize = "small"
            pass
        else:
            Megasize = input("Please enter yes or no: ").lower()
    elif ToppingSize == "medium":
        total_cost += 0.75
    elif ToppingSize == "large":
        total_cost += 1.00
    Topping = input("What topping would you like? Sprinkles, chocolate chips, or gummy bears? ")
    Topping = Topping.lower()
    while Topping not in ["sprinkles", "chocolate chips", "gummy bears"]:
        Topping = input("Please enter sprinkles, chocolate chips, or gummy bears: ").lower()
else:
    Topping = ""
YesorNoDrink = input("Would you like a drink? ")
YesorNoDrink = YesorNoDrink.lower()
DrinkList = ["yes", "no"]
while YesorNoDrink not in DrinkList:
    YesorNoDrink = input("Please enter yes or no: ").lower()
if YesorNoDrink == "yes":
    Size = input("What size drink would you like? Small ($1.00), Medium ($1.75), or Large ($2.25)? ")
    Size = Size.lower()
    Sizes = ["small", "medium", "large"]
    while Size not in Sizes:
        Size = input("Please enter small, medium, or large: ").lower()
    if Size == "small":
        total_cost += 1.00
    elif Size == "medium":
        total_cost += 1.75
    elif Size == "large":
        total_cost += 2.25
    Drink = input("What drink would you like? Lemonade, iced tea, or milkshake? ")
    Drink = Drink.lower()
    while Drink not in ["lemonade", "iced tea", "milkshake"]:
        Drink = input("Please enter lemonade, iced tea, or milkshake: ").lower()
else:
    Drink = ""
