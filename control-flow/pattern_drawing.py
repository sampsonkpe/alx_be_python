# Prompt the user to enter the size of the square pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer loop to iterate through each row using a while loop
while row < size:
    # Inner loop to print asterisks in each row using a for loop
    for _ in range(size):
        print("*", end="")  # Print asterisk without newline
    print()  # Move to the next line after printing a row
    row += 1  # Increment the row counter

