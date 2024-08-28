#write a program to print all the prime numbers which come in the range entered by the use
lower = int(input("Enter a lower range: "))
upper = int(input("Enter an upper range: "))

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)