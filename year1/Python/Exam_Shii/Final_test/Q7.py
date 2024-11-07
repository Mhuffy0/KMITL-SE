# You are given a dictionary `employee_salaries` where each key is an employee's name, and each
# value is their salary. Define a function `rank_employees(employee_salaries)` that returns a list of
# employee names ranked from highest to lowest salary. If two employees have the same salary, their
# order does not matter.
# Example:
# `rank_employees({'Alice': 50000, 'Bob': 45000, 'Eve': 50000})` -> `['Alice', 'Eve', 'Bob']`

emply = {"John":15000,
         'Dog':25000,
         'Ronaldo':999999
         }

def rank(empl):
    result = []
    temp = sorted(empl.items(), key=lambda item: item[1], reverse=True)
    
    for k,v in temp:
        result.append(k)
        
    return result

print(rank(emply))