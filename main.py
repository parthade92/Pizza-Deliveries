print("Welcome to Pizza Deliveries")
size = input("What size pizza do you want S, M, L? ").upper()
pep = input("Do you want pepperoni? Y or N: ").upper()
cheese = input("Do you want extra cheese? Y or N: ").upper()
bill = 0
if size == 'S':
    bill = 15
    if pep == 'Y':
        bill = bill + 2
    if cheese == 'Y':
        bill = bill + 1
elif size == 'M':
    bill = 20
    if pep == 'Y':
        bill = bill + 3
    if cheese == 'Y':
        bill = bill + 1
elif size == 'L':
    bill = 25
    if pep == 'Y':
        bill = bill + 3
    if cheese == 'Y':
        bill = bill + 1
print("Your Order")
print(f'Pizza Size: {size}\nPepperoni: {pep}\nExtra Cheese: {cheese}')
print(f"Your final bill is: ${bill}")

