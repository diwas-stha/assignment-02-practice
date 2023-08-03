'''
Write a Python function called check_odd_even that takes an integer as input and
uses a ternary operator to return "Even" if the number is even, and "Odd" if the
number is odd.

'''

def check_odd_even(num):
    """
    Check if the given number is even or odd using a ternary operator.

    Parameters:
        number (int): The integer number to check.
    
    Return:
        Even if number is even, odd if number is odd
    """

    return "Even" if num %2==0 else "Odd"

print(check_odd_even(10))  # Output: "Even"
print(check_odd_even(7))   # Output: "Odd"
print(check_odd_even(4))   # Output: "Even"
print(check_odd_even(-5))  # Output: "Odd"

