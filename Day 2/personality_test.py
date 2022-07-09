# Asking the user for the number of books
no_of_books = int(input('How many books hae you purchased?\n'))
# initializing the points variable
points = 0

# Setting the number of points based on the number of books purchased
if no_of_books == 1:
    points = 6
elif no_of_books == 2:
    points = 16
elif no_of_books == 3:
    points = 32
elif no_of_books >= 4:
    points = 60


# printing the number of books and points
print(f"Books: {no_of_books}\nPoints: {points}")
