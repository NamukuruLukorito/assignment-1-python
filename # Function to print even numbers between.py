# Function to print even numbers between two numbers
def print_even_numbers(start, end):
    print(f"Even numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if num % 2 == 0:
            print(num, end=" ")
    print()  # for new line

# Function to print numbers divisible by 2 between two numbers
def print_numbers_divisible_by_2(start, end):
    print(f"Numbers divisible by 2 between {start} and {end}:")
    for num in range(start, end + 1):
        if num % 2 == 0:
            print(num, end=" ")
    print()  # for new line

# Main function to take user input and call the above functions
def main():
    # Taking user input
    start = int(input("Enter the first number: "))
    end = int(input("Enter the second number: "))
    
    # Ensure start is less than end
    if start > end:
        start, end = end, start
    
    # Calling the functions
    print_even_numbers(start, end)
    print_numbers_divisible_by_2(start, end)

# Calling the main function
if __name__ == "__main__":
    main()
