'''
[**kwargs] Write a Python function calculate_total_cost that calculates the total
cost of items purchased from a store. The function should accept multiple keyword
arguments, where the key is the item name, and the value is the item's price. The
function should return the total cost of all items.

'''

# def calculate_total_cost(**kwargs):
#     total = sum(kwargs.values())
#     return total


# print(calculate_total_cost(apple=10, mango=15, banana=5))  

'''
[**kwargs] Create a function create_student_report that takes the student's
name as the first argument, the student's age as the second argument, and an
arbitrary number of keyword arguments for the subjects and their respective
scores. The function should return a dictionary with the student's information and a
list of subjects along with their scores.
'''

def create_student_report(name, age, **kwargs):
    student_report = {
        'name': name,
        'age': age,
        'subject': kwargs
    }
    return student_report

print(create_student_report('John Doe', 20, Math=95, Science=85, History=75))
print(create_student_report('Jane Smith', 18, English=80, Chemistry=90))
print(create_student_report('Bob Johnson', 19, Biology=88, Physics=92, Music=75))

