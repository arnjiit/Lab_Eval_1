employee_details = {}

def add_employee(name, empid, department, salary):
    if empid in employee_details:
        print(f"Employee {name} already exits.")
    else:
        employee_details[empid] = {
            'Name': name,
            'Department': department,
            'Salary': salary
        }
        print(f"Employee {name} added successfully.")

def update_details(empid, name=None, department=None, salary=None):
    if empid in employee_details:
        if name:
            employee_details[empid]['Name'] = name
        if department:
            employee_details[empid]['Department'] = department
        if salary:
            employee_details[empid]['Salary'] = salary
        print(f"Employee ID {empid} details' updated successfully.")
    else:
        print(f"Employee with {empid} doesn't exist.")

def search_employee(empid):
    if empid in employee_details:
        emp_details = employee_details[empid]
        print(f"Employee ID: {empid}")
        print(f"Employee Name: {emp_details['Name']}")
        print(f"Employee Department: {emp_details['Department']}")
        print(f"Employee Salary: {emp_details['Salary']}")
    else:
        print(f"Employee with ID {empid} doesn't exist.")

def department_report():
    dept_report = {}
    for empid, details in employee_details.items():
        department = details['Department']
        if department not in dept_report:
            dept_report[department] = []
        dept_report[department].append({
            'ID': empid,
            'Name': details['Name'],
            'Salary': details['Salary']
        })
    
    print(f"Department Wise Report:")
    for dept, emp in dept_report.items():
        print(f"\nDepartment: {department}\n")
        for e in emp:
            print(f"Emp ID: {e['ID']}, 'Name': {e['Name']}, 'Salary': {e['Salary']}")



add_employee('Arnav', 100, 'CSE', 10000)
add_employee('Charlie', 200, 'ECE', 20000)
add_employee('Harsh', 300, 'Bio', 30000)
print(employee_details)

update_details(200, name='newCharlie')
print(employee_details)

search_employee(300)
search_employee(200)

department_report()

update_details(200, department='asdfghjk')
print(employee_details)