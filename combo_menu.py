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
