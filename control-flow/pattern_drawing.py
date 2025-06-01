# pattern_drawing.py

# Prompt the user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use while loop for rows
while row < size:
    # Use for loop for columns
    for col in range(size):
        print("*", end="")
    # Move to the next line after printing one row
    print()
    row += 1
