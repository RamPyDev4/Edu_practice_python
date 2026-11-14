"""def calculate():
    
    a = 10
    b = 20
    result = a + b
    print(result)

    calculate()
    """
"""
def add_numbers():
    a = 10
    b = 20
    return a + b

result = add_numbers()
print(result)"""



"""def calculate_salary(basic_salary, bonus, deductions):
    total_salary = basic_salary + bonus
    final_salary = total_salary - deductions

    return final_salary


def display_employee(name, basic_salary, bonus, deductions):
    print("Employee:", name)

    salary = calculate_salary(basic_salary,
                            bonus,
                              deductions)

    print("Basic Salary:", basic_salary)
    print("Bonus:", bonus)
    print("Deductions:", deductions)
    print("Final Salary:", salary)


# Employee details
employee_name = "Rahul"
basic_salary = 30000
bonus = 5000
deductions = 3000

display_employee(employee_name,basic_salary,bonus,deductions)"""
"""
def calculate_total(price, quantity):
    total = price * quantity
    return total


def apply_discount(total):
    if total >= 1000:
        discount = total * 0.10

    final_amount = total - discount
    return final_amount


price = 300
quantity = 4

total = calculate_total(price, quantity)
final_amount = apply_discount(total)

print("Total:", total)
print("Final Amount:", final_amount)"""

"""
def get_employee(employee_id):

    employees = {
        101: {"name": "Rahul", "salary": 30000},
        102: {"name": "Arun", "salary": 40000},
        103: {"name": "Kiran", "salary": 50000}
    }

    return employees.get(employee_id)


def calculate_bonus(employee):

    salary = employee["salary"]

    if salary >= 40000:
        bonus = salary * 0.10
    else:
        bonus = salary * 0.05

    return bonus


def generate_employee_report(employee_id):

    employee = get_employee(employee_id)

    bonus = calculate_bonus(employee)

    final_salary = employee["salary"] + bonus

    print("Employee:", employee["name"])
    print("Final Salary:", final_salary)


generate_employee_report(101)"""


""""
def get_employee(employee_id):

    employees = {
        101: {"name": "Rahul", "salary": 30000},
        102: {"name": "Arun", "salary": 40000}
    }

    return employees.get(employee_id)


def calculate_bonus(salary):

    bonus = salary * 0.10

    return bonus


def calculate_final_salary(salary, bonus):

    final_salary = salary + bonus

    return final_salary


def generate_report(employee_id):

    employee = get_employee(employee_id)

    bonus = calculate_bonus(employee["salary"])

    final_salary = calculate_final_salary(
        employee["salary"],
        bonus
    )

    print("Employee:", employee["name"])
    print("Salary:", employee["salary"])
    print("Bonus:", bonus)
    print("Final Salary:", final_salary)


generate_report(101)"""
   
   
"""def calculate_salary(basic, bonus, deductions):

    total = basic + bonus
    final_salary = total - deductions

    return final_salary


def generate_report(name, basic, bonus, deductions):

    if deductions > 2000:
        print("HR review required for:", name)
        return

    salary = calculate_salary(
        basic,
        bonus,
        deductions
    )

    print("Employee:", name)
    print("Basic:", basic)
    print("Bonus:", bonus)
    print("Deductions:", deductions)
    print("Final Salary:", salary)


employees = [
    ("Rahul", 30000, 5000, 2000),
    ("Arun", 40000, 6000, 3000),
    ("Kiran", 35000, 4000, 1500)
]


for employee in employees:

    name = employee[0]
    basic = employee[1]
    bonus = employee[2]
    deductions = employee[3]

    generate_report(name, basic, bonus, deductions)
"""


def calculate_bonus(salary, attendance):


    if attendance >= 25:
        bonus = salary * 0.10
    elif attendance >= 20:
        bonus = salary * 0.05
    else:
        bonus = 0

    return bonus

def generate_report(name, salary, attendance):

    bonus = calculate_bonus(salary, attendance)

    final_salary = salary + bonus

    print("Employee:", name)
    print("Attendance:", attendance)
    print("Bonus:", bonus)
    print("Final Salary:", final_salary)
    print("--------------------")


employees = [
    ("Rahul", 30000, 26),
    ("Arun", 40000, 24),
    ("Kiran", 35000, 19),
    ("Ravi", 32000, 25)
]


for employee in employees:

    name = employee[0]
    salary = employee[1]
    attendance = employee[2]

    generate_report(name, salary, attendance)