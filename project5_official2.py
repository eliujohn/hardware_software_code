# Author: [Your Name]  
# Program Name: Decimal and Binary Converter  
# Purpose: This program converts decimal numbers to binary, binary numbers to decimal,  
#          and includes functionality for hexadecimal conversions.  
# Description: The program provides a menu for the user to choose the type of conversion.  
#              It validates the input and performs the conversion using loops.  

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

def hexadecimal_to_decimal(hexadecimal_number):  
    """Convert a hexadecimal number to a decimal number."""  
    decimal_result = 0  
    hexadecimal_number = hexadecimal_number.upper()  
    hex_chars = '0123456789ABCDEF'  
    
    for index, digit in enumerate(reversed(hexadecimal_number)):  
        decimal_result += hex_chars.index(digit) * (16 ** index)  
    
    return decimal_result  

def decimal_to_hexadecimal(decimal_number):  
    """Convert a decimal number to hexadecimal."""  
    hexadecimal_result = ""  
    while decimal_number > 0:  
        remainder = decimal_number % 16  
        if remainder < 10:  
            hexadecimal_result = str(remainder) + hexadecimal_result  
        else:  
            # Convert to hexadecimal character (A-F)  
            hexadecimal_result = chr(ord('A') + remainder - 10) + hexadecimal_result  
        decimal_number = decimal_number // 16  
    return hexadecimal_result if hexadecimal_result else "0"  

def is_valid_binary(binary_number):  
    """Check if the input is a valid binary number."""  
    return all(char in '01' for char in binary_number)  

def is_valid_decimal(decimal_number):  
    """Check if the input is a valid decimal number."""  
    return decimal_number.isdigit()  

def is_valid_hexadecimal(hexadecimal_number):  
    """Check if the input is a valid hexadecimal number."""  
    return all(char in '0123456789ABCDEFabcdef' for char in hexadecimal_number)  

def main():  
    print("Welcome to the Decimal and Binary Converter Program!")  
    while True:  
        print("\nMenu:")  
        print("1. Convert Binary to Decimal")  
        print("2. Convert Decimal to Binary")  
        print("3. Convert Hexadecimal to Decimal")  
        print("4. Convert Decimal to Hexadecimal")  
        print("5. Quit")  
        
        choice = input("Please make a selection (1, 2, 3, 4, or 5): ")  
        
        if choice == '1':  
            binary_number = input("Enter a binary number: ")  
            if is_valid_binary(binary_number):  
                decimal_result = binary_to_decimal(binary_number)  
                print(f"Binary {binary_number} is Decimal {decimal_result}")  
            else:  
                print("Invalid binary number. Please try again.")  
        
        elif choice == '2':  
            decimal_number = input("Enter a decimal number: ")  
            if is_valid_decimal(decimal_number):  
                binary_result = decimal_to_binary(int(decimal_number))  
                print(f"Decimal {decimal_number} is Binary {binary_result}")  
            else:  
                print("Invalid decimal number. Please try again.")  
        
        elif choice == '3':  
            hexadecimal_number = input("Enter a hexadecimal number: ")  
            if is_valid_hexadecimal(hexadecimal_number):  
                decimal_result = hexadecimal_to_decimal(hexadecimal_number)  
                print(f"Hexadecimal {hexadecimal_number} is Decimal {decimal_result}")  
            else:  
                print("Invalid hexadecimal number. Please try again.")  
        
        elif choice == '4':  
            decimal_number = input("Enter a decimal number: ")  
            if is_valid_decimal(decimal_number):  
                hexadecimal_result = decimal_to_hexadecimal(int(decimal_number))  
                print(f"Decimal {decimal_number} is Hexadecimal {hexadecimal_result}")  
            else:  
                print("Invalid decimal number. Please try again.")  
        
        elif choice == '5':  
            print("Thank you for using the converter. Goodbye!")  
            break  
        
        else:  
            print("Invalid selection. Please try again.")  

# Call the main function to run the program  
if __name__ == "__main__":  
    main()
