# Author: [Your Name]
# Program Name: Decimal and Binary Converter
# Purpose: This program converts decimal numbers to binary and binary numbers to decimal.
# Description: The program provides a menu for the user to choose the type of conversion.
# It validates the input and performs the conversion using loops.

def binary_to_decimal(binary_number):
    """Convert a binary number to a decimal number."""
    decimal_result = 0
    power = len(binary_number) - 1
    for digit in binary_number:
        decimal_result += int(digit) * (2 ** power)
        power -= 1
    return decimal_result

def decimal_to_binary(decimal_number):
    """Convert a decimal number to a binary number."""
    binary_result = ""
    while decimal_number > 0:
        binary_result = str(decimal_number % 2) + binary_result
        decimal_number = decimal_number // 2
    return binary_result if binary_result else "0"

def is_valid_binary(binary_number):
    """Check if the input is a valid binary number."""
    return all(char in '01' for char in binary_number)

def is_valid_decimal(decimal_number):
    """Check if the input is a valid decimal number."""
    return decimal_number.isdigit()

def main():
    print("Welcome to the Decimal and Binary Converter Program!")
    while True:
        print("\nMenu:")
        print("1. Convert Binary to Decimal")
        print("2. Convert Decimal to Binary")
        print("3. Quit")
        choice = input("Please make a selection (1, 2, or 3): ")

        if choice == '1':
            binary_number = input("Enter a binary number: ")
            if is_valid_binary(binary_number):
                decimal_result = binary_to_decimal(binary_number)
                print(f"Binary {binary_number} is Decimal {decimal_result}")
            else:
                print("Invalid binary number. Please try again.")
        elif choice == '2':
            decimal_number = input("Enter a
