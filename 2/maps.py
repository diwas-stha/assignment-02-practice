'''
[map] Write a Python function square_numbers that takes a list of integers as
input and uses the map function to return a new list containing the square of each
element
'''
def square_numbers(integers):
    """
    Compute the square of each element in the input list.

    Parameters:
        The list of integers.

    """
    squared_list = list(map(lambda x: x**2, integers))
    return squared_list

print(square_numbers([1,2,3,4,5,6])) #output [1,4,9,16,25,36]