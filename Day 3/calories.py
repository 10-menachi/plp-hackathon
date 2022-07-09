# getting how many grams of both fats and carbs the user has consumed
fat_grams = int(input("How many grams of fats hae you consumed? "))

carb_grams = int(input("How many grams of carbs hae you consumed? "))

# calculating the number of calories from both fats and carbs
calories_from_fats = fat_grams * 9

calories_from_carbs = carb_grams * 4

# displaying the number of calories to the user
print(f"Total Calories from fats = {calories_from_fats}")

print(f"Total Calories from carbs = {calories_from_carbs}")