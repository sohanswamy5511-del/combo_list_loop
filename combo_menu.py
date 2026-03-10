orders = []    # each entry will be dict with description and cost
while True:
    flavor = ""
    ToppingSize = ""
    Topping = ""
    Size = ""
    Drink = ""
    servings = 0
    cost = 0.0
    
    flavor = input("What ice cream flavor would you like? Vanilla ($3.00), Chocolate ($3.25), or Strawberry ($3.50)? ")
    flavors = ["vanilla", "chocolate", "strawberry"]
    flavor = flavor.lower()
    while flavor not in flavors:
        flavor = input("Please enter Vanilla, Chocolate, or Strawberry: ").lower()
    if flavor == "vanilla":
        cost = 3.00
    elif flavor == "chocolate":
        cost = 3.25
    elif flavor == "strawberry":
        cost = 3.50

    YesorNoToppings = input("Would you like toppings? ").lower()
    while YesorNoToppings not in ["yes", "no"]:
        YesorNoToppings = input("Please enter yes or no: ").lower()
    if YesorNoToppings == "yes":
        ToppingSize = input("What size topping portion would you like? Small ($0.50), Medium ($0.75), or Large ($1.00)? ")
        ToppingSize = ToppingSize.lower()
        ToppingSizes = ["small", "medium", "large"]
        while ToppingSize not in ToppingSizes:
            ToppingSize = input("Please enter small, medium, or large: ").lower()
        if ToppingSize == "small":
            cost += 0.50
            MegaSize = input("Would you like to mega size your toppings for an extra $0.50? ").lower()
            while MegaSize not in ["yes", "no"]:
                MegaSize = input("Please enter yes or no: ").lower()
            if MegaSize == "yes":
                cost += 0.50
                ToppingSize = "large"
            else:
                ToppingSize = "small"
        elif ToppingSize == "medium":
            cost += 0.75
        elif ToppingSize == "large":
            cost += 1.00
        Topping = input("What topping would you like? Sprinkles, chocolate chips, or gummy bears? ")
        Topping = Topping.lower()
        while Topping not in ["sprinkles", "chocolate chips", "gummy bears"]:
            Topping = input("Please enter sprinkles, chocolate chips, or gummy bears: ").lower()
    
    YesorNoDrink = input("Would you like a drink? ").lower()
    while YesorNoDrink not in ["yes", "no"]:
        YesorNoDrink = input("Please enter yes or no: ").lower()
    if YesorNoDrink == "yes":
        Size = input("What size drink would you like? Small ($1.00), Medium ($1.75), or Large ($2.25)? ")
        Size = Size.lower()
        Sizes = ["small", "medium", "large"]
        while Size not in Sizes:
            Size = input("Please enter small, medium, or large: ").lower()
        if Size == "small":
            cost += 1.00
        elif Size == "medium":
            cost += 1.75
        elif Size == "large":
            cost += 2.25
        Drink = input("What drink would you like? Lemonade, iced tea, or milkshake? ")
        Drink = Drink.lower()
        while Drink not in ["lemonade", "iced tea", "milkshake"]:
            Drink = input("Please enter lemonade, iced tea, or milkshake: ").lower()

    ConeType = input("What type cone would you like? Sugar cone ($0.50), Waffle cone ($0.75), or Cup ($0.25)? ")
    ConeType = ConeType.lower()
    ConeTypes = ["sugar cone", "waffle cone", "cup"]
    while ConeType not in ConeTypes:
        ConeType = input("Please enter sugar cone, waffle cone, or cup: ").lower()
    if ConeType == "sugar cone":
        cost += 0.50
    elif ConeType == "waffle cone":
        cost += 0.75
    elif ConeType == "cup":
        cost += 0.25

    WhippedCream = input("Would you like whipped cream? Enter number of servings (each serving costs $0.50): ")
    while True:
        try:
            servings = int(WhippedCream)
            if servings < 0:
                WhippedCream = input("Please enter a number 0 or above: ")
            elif servings >= 5:
                WhippedCream = input("Sorry, we cannot provide that many servings of whipped cream. Please enter a number less than 5: ")
            else:
                cost += 0.50 * servings
                break
        except ValueError:
            WhippedCream = input("Please enter a valid number: ")

    #build order description
    description = f'{flavor} ice cream'
    if Topping:
        description += f' with {ToppingSize} {Topping}'
    if Drink:
        description += f' and a {Size} {Drink}'
    description += f' in a {ConeType}'
    if servings > 0:
        description += f' with {servings} servings of whipped cream'
    if Topping and Drink:
        discount = 1.00
        cost -= discount
        description += f' (includes $1.00 combo discount)'
        
    orders.append({"description": description, "cost": cost})
        
    another = input("Would you like to add another ice cream order? (yes/no) ").lower()
    while another not in ["yes", "no"]:
        another = input("Please enter yes or no: ").lower()
    if another == "no":
        break
print("--- Order Summary ---")
for order in orders:
    i = 1
    while i < len(orders) + 1:
        print(f'{i}. {order['description']}: Cost of ${order['cost']:.2f}')
        i += 1
    total_cost_orders = sum(order['cost'] for order in orders)
    print(f"Total cost of all orders: ${total_cost_orders:.2f}")
