# Name   : Umar Hilmi
# NIM    : 221402077
# KOM    : B2
# Number : 5

numbers = []
while True:
    try:
        number_input = int(input("Input number (or -1 to quit): "))

        if number_input != -1:
            numbers.append(number_input)
        else:
            break
    except ValueError:
        print("Invalid input. Enter an integer.")

total = sum(numbers)

print(f"The sum of all entered numbers = {total}")
print("List of entered numbers =", *numbers)
