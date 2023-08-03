'''
[*args] Write a Python function that takes an arbitrary number of positional
arguments and returns the sum of all the numbers. Test your function with various
input cases.

'''
def addition(*args):
    """
    Calculate the sum of an arbitrary number of positional arguments.

    Parameters:
        *args (float or int): Any number of positional arguments.

    Returns:
        float or int: The sum of all the positional arguments.
    """

    return sum(args)


print(addition(1, 2, 3))  # Output: 6 (1 + 2 + 3 = 6)
print(addition(10, 20, 30, 40))  # Output: 100 (10 + 20 + 30 + 40 = 100)
print(addition(2, 4, 6, 8, 10))  # Output: 30 (2 + 4 + 6 + 8 + 10 = 30)
print(addition())  # Output: 0 (No arguments passed, so the sum is 0)
print(addition(5))  # Output: 5 (Only one argument, so the sum is 5)
