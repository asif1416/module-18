# Input the value of terms
n = int(input("Enter the value of terms: "))

sum = 0  # Initialize the sum to 0
i = 1    # Initialize the counter to 1

while i <= n:  # Loop will run from 1 to n
    sum = sum + i  # Add the current value of i to the sum
    i = i + 1      # Increment the counter

print("\nSum =", sum)