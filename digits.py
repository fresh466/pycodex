"""
digits.py: Inspired from 'The Reciprocals of Prime' by Numberphile.
Generated with Codex as part of the PyCodex project.
"""
import sys

def main():
    """
    Main function
    """
    # Get the fraction from the user
    fraction = input("Enter a fraction: ")
    
    # Split the fraction into the numerator and denominator
    numerator, denominator = fraction.split("/")
    
    # Convert the numerator and denominator into integers
    numerator = int(numerator)
    denominator = int(denominator)
    
    # Calculate the number of digits it takes to hit every possible digit before it loops
    digits = calculate_digits(numerator, denominator)
    
    # Print the result
    print("It takes {} digits to hit every possible digit until it loops.".format(digits))
    
def calculate_digits(numerator, denominator):
    """
    Calculate the number of digits it takes to hit every possible digit until it loops.
    """
    # Initialize the number of digits
    digits = 0
    
    # Initialize the list of digits
    digits_list = []
    
    # Initialize the remainder
    remainder = numerator % denominator
    
    # Loop until the remainder is 0
    while remainder != 0:
        # Increment the number of digits
        digits += 1
        
        # Calculate the next digit
        next_digit = (remainder * 10) // denominator
        
        # Add the next digit to the list of digits
        digits_list.append(next_digit)
        
        # Calculate the next remainder
        remainder = (remainder * 10) % denominator
        
        # Check if the remainder is already in the list of digits
        if remainder in digits_list:
            # Break the loop
            break
    # Return the number of digits
    return digits
    
if __name__ == "__main__":
    sys.exit(main())
