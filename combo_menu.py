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
ConeType = input("What type cone would you like? Sugar cone ($0.50), Waffle cone ($0.75), or Cup ($0.25)? ")
ConeType = ConeType.lower()
ConeTypes = ["sugar cone", "waffle cone", "cup"]
while ConeType not in ConeTypes:
    ConeType = input("Please enter sugar cone, waffle cone, or cup: ").lower()
    if ConeType == "sugar cone":
        total_cost += 0.50
    elif ConeType == "waffle cone":
        total_cost += 0.75
    elif ConeType == "cup":
        total_cost += 0.25
    else:
        ConeType = input("Please enter sugar cone, waffle cone, or cup: ").lower()
WhippedCream = int(input("Would you like whipped cream? Enter number of servings (each serving costs $0.50): "))
if WhippedCream < 0:
    print("Please enter a number 0 or above: ")
elif WhippedCream >= 5:
    print("Sorry, we cannot provide that many servings of whipped cream. Please enter a number less than 5: ")
elif not isinstance(WhippedCream, int):
    input("Please enter a valid number: ")
else:
    total_cost += 0.50 * int(WhippedCream)
    print(f'You ordered {WhippedCream} servings of whipped cream. That brings your total cost to ${total_cost}')
if flavor != "" and Topping != "" and Drink != "":
    total_cost -= 0.50
    print(f"You ordered a {flavor} ice cream with {Topping}, and a {Size}{Drink}")
    print(f"Since you got ice cream with toppings and a drink, your total cost is deducted $0.50. That means your order costs ${total_cost}")
elif flavor != "" and Topping != "":
    print(f"You ordered a {flavor} ice cream in a {ConeType} with {Topping}")
    print(f"Your total cost is ${total_cost}")
elif flavor != "" and Drink != "":
    print(f'You ordered a {flavor} ice cream and a {Size}{Drink}')
    print(f"Your total cost is ${total_cost}")
