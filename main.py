print("Welcome to Pizza Deliveries")
size = input("What size pizza do you want S, M, L? ")
pep = input("Dp you want pepperoni? Y or N: ")
cheese = input("Dp you want extra cheese? Y or N: ")
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
print(f"Your final bill is: ${bill}")

