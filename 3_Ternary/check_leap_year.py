'''
Create a Python function check_leap_year that takes a year as input and uses a
ternary operator to determine if it's a leap year. Return "Leap Year" if it is, otherwise
"Not a Leap Year." (A leap year is divisible by 4, except for years divisible by 100
but not divisible by 400).
'''

def check_leap_year(year):
    '''
    Check if the given year is a leap year

    Parameter:
        year (int) : input year to check
    
    Return:
        Leap Year if year is leap year, else Not a leap year
    '''

    return "Leap year" if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else "Not a Leap year"

print(check_leap_year(2020))  # Output: "Leap Year"
print(check_leap_year(2021))  # Output: "Not a Leap Year"
print(check_leap_year(2000))  # Output: "Leap Year"
print(check_leap_year(1998))  # Output: "Not a Leap Year"
print(check_leap_year(1900))  # Output: "Not a Leap Year"
print(check_leap_year(1600))  # Output: "Leap Year"
