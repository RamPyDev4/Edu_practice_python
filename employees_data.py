
employees = [
    {
        "employee_id": i,
        "name": f"Employee_{i:03d}",
        "gross_salary": 30000 + (i % 15) * 2500
    }
    for i in range(1, 151)  
]
