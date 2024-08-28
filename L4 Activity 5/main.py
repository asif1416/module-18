# Input from the user
decimal_number = int(input("Enter a decimal number: "))

# Initialize an empty string to store the binary representation
binary_number = ""

# Handle the special case when the input is 0
if decimal_number == 0:
    binary_number = "0"
else:
    # Convert decimal to binary
    while decimal_number > 0:
        binary_digit = decimal_number % 2  # Get the remainder when dividing by 2
        binary_number = str(binary_digit) + binary_number  # Prepend the binary digit
        decimal_number = decimal_number // 2  # Divide the number by 2 for the next iteration

# Output the binary representation
print("Binary representation is", binary_number)
