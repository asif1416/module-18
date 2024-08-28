#write a program to calculate the product of the middle digits of a number
num = int(input("Enter a number: "))

num_len = len(str(num))
if num_len >= 4:
    mid_index = num_len // 2
    mid_one = num // (10 ** (mid_index - 1)) % 10
    if num_len % 2 == 0:
        mid_two = num // (10 ** mid_index) % 10
    else:
        mid_two = mid_one
    product = mid_one * mid_two
    print("Product of middle digits:", product)
else:
    print("It's not a 4 or more than 4-digit number!")