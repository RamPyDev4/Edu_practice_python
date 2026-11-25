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

    generate_report(name, salary, attendance)"""
    
    
"""def calculate_total(price, quantity):
    total = price * quantity
    return total


def generate_invoice(product, price, quantity):
    total = calculate_total(price, quantity)

    print("Product:", product)
    print("Price:", price)
    print("Quantity:", quantity)
    print("Total:", total)


generate_invoice("Laptop", 50000, 2)"""

"""def calculate_order_total(items):
    total = 0

    for item in items:
        total += item["price"]

    return total


items = [
    {"product": "Laptop", "price": 50000},
    {"product": "Mouse", "price": 1000},
    {"product": "Keyboard", "price": 2000}
]

order_total = calculate_order_total(items)

print("Order Total:", order_total)"""


"""def get_active_customers(customers):



    active_customers = []

    for customer in customers:
        if customer["is_active"] == True:
            active_customers.append(customer)

    return active_customers


customers = [
    {"id": 101, "name": "Rahul", "is_active": True},
    {"id": 102, "name": "Arun", "is_active": False},
    {"id": 103, "name": "Kiran", "is_active": True},
    {"id": 104, "name": "Ravi", "is_active": False}
]

result = get_active_customers(customers)

print("Active Customers:", result)
print("Total Active Customers:", len(result))"""




"""def calculate_delivery_charge(order_amount):
    delivery_charge = 50

    if order_amount >= 1000:
        delivery_charge = 0

    return delivery_charge


orders = [
    {"order_id": 101, "customer": "Rahul", "amount": 999},
    {"order_id": 102, "customer": "Arun", "amount": 600},
    {"order_id": 103, "customer": "Kiran", "amount": 1001},
    {"order_id": 104, "customer": "Ravi", "amount": 1002}
]

for order in orders:
    charge = calculate_delivery_charge(order["amount"])

    print("Customer:", order["customer"])
    print("Order Amount:", order["amount"])
    print("Delivery Charge:", charge)
    print("--------------------")"""
    
    
"""
def calculate_bonus(attendance):
    if attendance >= 26:
        return 3000
    else:
        return 0
def calculate_tax(gross_salary):
    tax = gross_salary * 0.10
    return tax
def calculate_salary(basic_salary, attendance):
    bonus = calculate_bonus(attendance)

    gross_salary = basic_salary + bonus

    tax = calculate_tax(gross_salary)

    final_salary = gross_salary - tax

    return final_salary
def generate_report(name, basic_salary, attendance):
    salary = calculate_salary(basic_salary, attendance)
    print("Employee:", name)
    print("Basic Salary:", basic_salary)
    print("Attendance:", attendance)
    print("Final Salary:", salary)
    print("------------------------")
generate_report("Rahul", 30000, 26)
generate_report("Arun", 40000, 24)
generate_report("Kiran", 35000, 28)"""

"""


def calculate_subtotal(price, quantity):
    subtotal = price * quantity
    return subtotal


def calculate_discount(subtotal):
    if subtotal >= 5000:
        discount = subtotal * 0.10
    else:
        discount = 0

    return discount


def calculate_final_amount(subtotal):
    discount = calculate_discount(subtotal)

    final_amount = subtotal - discount

    return final_amount
def generate_bill(customer, price, quantity):
    subtotal = calculate_subtotal(price, quantity)
    final_amount = calculate_final_amount(subtotal)
    print("Customer:", customer)
    print("Subtotal:", subtotal)
    print("Final Amount:", final_amount)
    print("------------------------")
generate_bill("Rahul", 3000, 2)
generate_bill("Arun", 2000, 2)
generate_bill("Kiran", 1500, 4)"""




"""def calculate_subtotal(price, quantity):
    subtotal = price * quantity
    return subtotal


def calculate_delivery_charge(subtotal):
    if subtotal >= 1000:
        return 0
    else:
        return 50


def calculate_final_amount(subtotal, quantity):
    delivery_charge = calculate_delivery_charge(quantity)

    final_amount = subtotal + delivery_charge

    return final_amount


def generate_bill(customer, price, quantity):
    subtotal = calculate_subtotal(price, quantity)

    final_amount = calculate_final_amount(subtotal, quantity)

    print("Customer:", customer)
    print("Subtotal:", subtotal)
    print("Final Amount:", final_amount)
    print("------------------------")


generate_bill("Rahul", 400, 3)
generate_bill("Arun", 200, 2)
generate_bill("Kiran", 250, 4)

"""


"""
def calculate_bonus(attendance):
    if attendance >= 26:
        return 3000
    elif attendance >= 22:
        return 2000
    else:
        return 0


def calculate_salary(basic_salary, attendance):
    bonus = calculate_bonus(attendance)

    final_salary = basic_salary + bonus

    return final_salary


def generate_report(name, basic_salary, attendance):
    final_salary = calculate_salary(basic_salary, attendance)

    print("Employee:", name)
    print("Attendance:", attendance)
    print("Basic Salary:", basic_salary)
    print("Final Salary:", final_salary)
    print("------------------------")


generate_report("Rahul", 30000, 26)
generate_report("Arun", 40000, 24)
generate_report("Kiran", 35000, 20)
"""
"""
def calculate_bonus(attendance, rating):

    if attendance >= 22:
        if rating == 5:
            bonus = 5000
        elif rating == 4:
            bonus = 3000
        elif rating == 3:
            bonus = 1000
        else:
            bonus = 0
    else:
        bonus = 0

    return bonus


def calculate_salary(basic_salary, attendance, rating):

    bonus = calculate_bonus(attendance, rating)

    final_salary = basic_salary + bonus

    return final_salary


def generate_report(name, basic_salary, attendance, rating):

    final_salary = calculate_salary(basic_salary, attendance, rating)

    print("Employee:", name)
    print("Attendance:", attendance)
    print("Rating:", rating)
    print("Final Salary:", final_salary)
    print("------------------------")


generate_report("Rahul", 30000, 25, 5)
generate_report("Arun", 40000, 21, 4)
generate_report("Kiran", 35000, 24, 3)
"""

"""
def calculate_discount(order_amount, customer_type):

    if order_amount >= 5000:
        if customer_type == "premium":
            discount = order_amount * 0.20
        else:
            discount = order_amount * 0.10
    else:
        if customer_type == "premium":
            discount = order_amount * 0.10
        else:
            discount = 0

    return discount


def calculate_final_amount(order_amount, customer_type):

    discount = calculate_discount(order_amount, customer_type)

    final_amount = order_amount - discount

    return final_amount


def generate_bill(name, order_amount, customer_type):

    final_amount = calculate_final_amount(order_amount, customer_type)

    print("Customer:", name)
    print("Order Amount:", order_amount)
    print("Customer Type:", customer_type)
    print("Final Amount:", final_amount)
    print("------------------------")


generate_bill("Rahul", 6000, "premium")
generate_bill("Arun", 6000, "regular")
generate_bill("Kiran", 3000, "premium")
generate_bill("Ravi", 3000, "regular")"""



"""""def calculate_total_salary(salaries):

    total_salary = 0

    for salary in salaries:
        total_salary = total_salary + salary

    return total_salary


def generate_report(salaries):

    total = calculate_total_salary(salaries)

    print("Employee Salaries:", salaries)
    print("Total Salary:", total)


salaries = [30000, 40000, 35000, 25000]

generate_report(salaries)"""""

"""from orders_data import orders

print(len(orders))

def calculate_total(orders):

    total = 0

    for order in orders:
        if order["status"] != "cancelled":
            total = total + order["amount"]

    return total


def generate_report(orders):

    total_amount = calculate_total(orders)

    print("Total Completed Orders:", total_amount)


generate_report(orders)"""


""""from employees_data import employees

print("Total Employees:", len(employees))

from employees_data import employees


def calculate_tax(gross_salary):

    tax = gross_salary * 0.10

    return tax


def calculate_net_salary(gross_salary):

    tax_amount = calculate_tax(gross_salary)

    net_salary = gross_salary - tax_amount

    return net_salary


def generate_report(employee):

    gross_salary = employee["gross_salary"]

    net_salary = calculate_net_salary(gross_salary)

    print("Employee ID:", employee["employee_id"])
    print("Employee Name:", employee["name"])
    print("Gross Salary:", gross_salary)
    print("Net Salary:", net_salary)
    print("------------------------")


for employee in employees:
    generate_report(employee)"""
    
    
    
""""from employees_data import employees

tax_rate = 0.10


def calculate_tax(gross_salary):

    ##tax_rate = 0.05

    tax = gross_salary * tax_rate

    return tax


def calculate_net_salary(gross_salary):

    tax_amount = calculate_tax(gross_salary)

    net_salary = gross_salary - tax_amount

    return net_salary, tax_amount


def generate_payroll(employees):

    total_gross = 0
    total_tax = 0
    total_net = 0

    for employee in employees:

        gross_salary = employee["gross_salary"]

        net_salary, tax_amount = calculate_net_salary(gross_salary)

        total_gross += gross_salary
        total_tax += tax_amount
        total_net += net_salary
        # Validation check
        expected_tax = gross_salary * 0.10
        expected_net = gross_salary - expected_tax

        if tax_amount != expected_tax:
            print(f"Tax mismatch for {employee['name']}")
            print(f"Expected tax: {expected_tax}")
            print(f"Actual tax: {tax_amount}")

        if net_salary != expected_net:
            print(f"Net salary mismatch for {employee['name']}")
            print(f"Expected net salary: {expected_net}")
            print(f"Actual net salary: {net_salary}")

    print("Total Employees:", len(employees))
    print("Total Gross Salary:", total_gross)
    print("Total Tax:", total_tax)
    print("Total Net Salary:", total_net)


generate_payroll(employees)"""

"""
from payments_data import payments


def calculate_processing_fee(amount):

    fee = amount * 0.02

    return fee


def calculate_final_amount(amount, fee):

    final_amount = amount - fee

    return final_amount


def process_payments(payments):

    successful_payments = 0
    total_amount = 0
    
    for payment in payments:
        try:
            payment_id = payment["payment_id"]
            amount = payment["amount"]

            if amount is None:
                raise ValueError(f"Payment ID {payment_id} has no amount.")

            fee = calculate_processing_fee(amount)

            final_amount = calculate_final_amount(amount, fee)

            successful_payments += 1
            total_amount += final_amount

            print("Payment ID:", payment_id)
            print("Final Amount:", final_amount)
            print("----------------------")
    
        except ValueError as e:
            print("Error processing payment:", e)
            continue


    print("Successful Payments:", successful_payments)
    print("Total Processed Amount:", total_amount)


process_payments(payments)"""

""""
from orders1 import orders
from order_service import generate_invoice



for order in orders:

    invoice = generate_invoice(order)

    print("Order ID:", invoice["order_id"])
    print("Customer Type:", invoice["customer_type"])
    print("Subtotal:", invoice["subtotal"])
    print("Discount:", invoice["discount"])
    print("Final Amount:", invoice["final_amount"])
    print("-----------------------------")"""
    
from sales_data import orders


def calculate_order_total(items):
    order_total = 0

    for item in items:
        item_total = item["quantity"] * item["price"]
        order_total += item_total

    return order_total


def generate_sales_report(orders):

    customer_sales = {}
    total_sales = 0

    for order in orders:

        if order["status"] == "delivered":

            customer = order["customer"]

            order_total = calculate_order_total(order["items"])

            customer_sales[customer] = order_total

            total_sales += order_total

    print("Customer Sales Report")

    for customer, amount in customer_sales.items():
        print(customer, ":", amount)

    print("----------------------")
    print("Total Delivered Sales:", total_sales)


generate_sales_report(orders)