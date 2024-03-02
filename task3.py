# Name   : Umar Hilmi
# NIM    : 221402077
# KOM    : B2
# Number : 3

number = int(input("Enter a number to check: "))

if number < 100:
    category = "Small"
elif number <= 200:
    category = "Medium"
else:
    category = "Large"

print(f"The number {number} is in the {category} category")