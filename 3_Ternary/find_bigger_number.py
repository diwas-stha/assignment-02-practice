'''
Write a function find_bigger_number that takes three integers as input and uses a
ternary operator to return the larger number. If all numbers are equal, return
"Equal."
'''

def find_bigger_number(a, b, c):
    '''
    Find the biggest number among the three inputs

    Parameter
        a, b, c (int): three integers 
    
    Return:
        Equal if a == b == c, else the bigger number
    '''

    return "Equal" if a == b == c else (a if a > b and a > c else b if b > c else c) 

print(find_bigger_number(3,3,3))
print(find_bigger_number(3,3,2))
print(find_bigger_number(3,5,10))
