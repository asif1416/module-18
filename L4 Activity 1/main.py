#write a program to check how many times a charachter is repeated in a word
string = input("Enter a word: ")
char = input("Enter a character: ")

count = 0
for letter in string:
    if letter == char:
        count += 1

print("The character", char, "occurs", count, "times in the string.")