def to_8bit_binary(number):
    # Format number to 8-bit binary
    return format(number if number >= 0 else (1 << 8) + number, '08b')

def ones_complement(binary):
    # Calculate one's complement
    return ''.join('1' if bit == '0' else '0' for bit in binary)

def twos_complement(binary):
    # Calculate two's complement
    ones_comp = ones_complement(binary)
    binary_int = int(ones_comp, 2)
    # Adding one to one's complement
    twos_comp = binary_int + 1
    # Ensuring the result is an 8-bit binary
    return format(twos_comp, '08b')

def binary_subtraction(minuend, subtrahend):
    # Convert decimal to 8-bit binary
    minuend_bin = to_8bit_binary(minuend)
    subtrahend_bin = to_8bit_binary(subtrahend)

    # Calculate two's complement of the subtrahend
    subtrahend_twos_comp = twos_complement(subtrahend_bin)

    # Perform binary addition of minuend and two's complement of subtrahend
    result = bin(int(minuend_bin, 2) + int(subtrahend_twos_comp, 2))

    # Result can exceed 8-bit, so we take only the last 8 bits
    result_bin = result[-8:]

    return {
        'minuend_bin': minuend_bin,
        'subtrahend_bin': subtrahend_bin,
        'subtrahend_twos_comp': subtrahend_twos_comp,
        'result_bin': result_bin,
        'result_dec': int(result_bin, 2) - (256 if result_bin[0] == '1' else 0)  # Convert back to signed integer
    }

if __name__ == "__main__":
    # Example: Change these numbers to test other cases.
    num1 = 120
    num2 = -25

    print(f"Number 1: {num1}")
    print(f"Number 2: {num2}\n")

    # One's and Two's Complementation
    for number in [num1, num2]:
        print(f"Number: {number}")
        binary = to_8bit_binary(number)
        print(f"8-bit Binary: {binary}")
        ones_comp = ones_complement(binary)
        print(f"One's Complement: {ones_comp}")
        twos_comp = twos_complement(binary)
        print(f"Two's Complement: {twos_comp}\n")

    # Subtraction
    print(f"Subtraction: {num1} - {num2}")
    result = binary_subtraction(num1, num2)
    print(f"Minuend Binary: {result['minuend_bin']}")
    print(f"Subtrahend Binary: {result['subtrahend_bin']}")
    print(f"Subtrahend Two's Complement: {result['subtrahend_twos_comp']}")
    print(f"Result Binary: {result['result_bin']}")
    print(f"Result Decimal: {result['result_dec']}")
