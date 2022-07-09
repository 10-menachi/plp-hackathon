# Taking input from the user which is the space to be covered and the price per paint
space = int(input("Enter the space to be painted: "))

price = int(input("Enter the price of paint per gallon: "))

# calculating the total gallons of paint and hours of labor required
gallons = space / 115

labor = 8 * gallons

# calculating the total cost of paint and cost of labor required
paintcost = price * gallons

laborcost = labor * 20

# Calculating the total cost of the paint job
totalcost = laborcost + paintcost

# Displaying the needed details to the user
print(f"You're gonna need:\n{gallons} gallons of paint\n{labor} hours of labor")

print(f"It'll cost you:\n{paintcost} ksh worth of paint")

print(f"{laborcost} ksh worth of labor.")

print(f"\n\nTotal cost will be {totalcost}")
