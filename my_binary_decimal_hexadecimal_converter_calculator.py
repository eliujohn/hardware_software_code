# Helper functions for conversions
def binary_to_decimal(binary_str):
    steps = []
    decimal_number = 0
    binary_str = binary_str[::-1]
    for i, digit in enumerate(binary_str):
        steps.append(f"{digit} * (2 ** {i}) = {int(digit) * (2 ** i)}")
        decimal_number += int(digit) * (2 ** i)
    return decimal_number, steps

def decimal_to_binary(decimal_number):
    steps = []
    binary_str = ""
    while decimal_number > 0:
        remainder = decimal_number % 2
        steps.append(f"{decimal_number} // 2 = {decimal_number // 2}, remainder = {remainder}")
        binary_str = str(remainder) + binary_str
        decimal_number //= 2
    return binary_str, steps

def hexadecimal_to_decimal(hex_str):
    steps = []
    decimal_number = 0
    hex_str = hex_str[::-1]
    for i, digit in enumerate(hex_str):
        digit_value = int(digit, 16)
        steps.append(f"{digit} * (16 ** {i}) = {digit_value * (16 ** i)}")
        decimal_number += digit_value * (16 ** i)
    return decimal_number, steps

def decimal_to_hexadecimal(decimal_number):
    steps = []
    hex_str = ""
    hex_digits = "0123456789ABCDEF"
    while decimal_number > 0:
        remainder = decimal_number % 16
        steps.append(f"{decimal_number} // 16 = {decimal_number // 16}, remainder = {hex_digits[remainder]}")
        hex_str = hex_digits[remainder] + hex_str
        decimal_number //= 16
    return hex_str, steps

def binary_to_hexadecimal(binary_str):
    decimal_number, binary_steps = binary_to_decimal(binary_str)
    hex_str, hex_steps = decimal_to_hexadecimal(decimal_number)
    return hex_str, binary_steps + ["->"] + hex_steps

def hexadecimal_to_binary(hex_str):
    decimal_number, hex_steps = hexadecimal_to_decimal(hex_str)
    binary_str, binary_steps = decimal_to_binary(decimal_number)
    return binary_str, hex_steps + ["->"] + binary_steps

# Main function to run the calculator
def calculator():
    while True:
        print("\nBinary, Hexadecimal and Decimal Converter")
        print("1: Convert to Binary")
        print("2: Convert to Hexadecimal")
        print("3: Convert to Decimal")
        print("4: Exit")
        choice = input("Choose an option (1/2/3/4): ")
        
        if choice == '4':
            print("Exiting the program.")
            break
        
        number = input("Enter the number: ")
        
        if choice == '1':
            if number.startswith('0x'):
                result, steps = hexadecimal_to_binary(number[2:])
                original = "hexadecimal"
            else:
                result, steps = decimal_to_binary(int(number))
                original = "decimal"
            print(f"Converting {number} from {original} to binary:")
        elif choice == '2':
            if number.startswith('0b'):
                result, steps = binary_to_hexadecimal(number[2:])
                original = "binary"
            else:
                result, steps = decimal_to_hexadecimal(int(number))
                original = "decimal"
            print(f"Converting {number} from {original} to hexadecimal:")
        elif choice == '3':
            if number.startswith('0b'):
                result, steps = binary_to_decimal(number[2:])
                original = "binary"
            elif number.startswith('0x'):
                result, steps = hexadecimal_to_decimal(number[2:])
                original = "hexadecimal"
            print(f"Converting {number} from {original} to decimal:")
        else:
            print("Invalid choice. Please choose 1, 2, 3, or 4.")
            continue
        
        for step in steps:
            print(step)
        print(f"Result: {result}")

if __name__ == "__main__":
    calculator()
