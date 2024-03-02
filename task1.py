# Name   : Umar Hilmi
# NIM    : 221402077 
# KOM    : B2
# Number : 1

import math

salary_per_year = float(input("Enter your annual salary: "))
salary_per_month = math.ceil(salary_per_year / 12)

print(f"Your monthly salary = Rp{salary_per_month:,}.")
