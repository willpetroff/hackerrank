"""
Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip),
and tax percent (the percentage of the meal price being added as tax) for a meal,
find and print the meal's total cost (rounded to the nearest integer).
"""

meal_cost = float(input())
meal_tip = int(input())
meal_tax = int(input())
meal_total = meal_cost + (meal_cost * (meal_tip/100) + (meal_cost * (meal_tax/100)))
print("The total meal cost is {} dollars.".format(int(round(meal_total))))