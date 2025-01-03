# employee_management_system.py

# Step 1: Initialize the employee data storage
employees = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},
    102: {'name': 'John', 'age': 30, 'department': 'IT', 'salary': 60000},
}

def main_menu():
    while True:
        print("\n--- Employee Management System ---")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")
        
        choice = input("Please choose an option (1-4): ")
        
        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            print("Thank you for using the Employee Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def add_employee():
    emp_id = int(input("Enter Employee ID: "))
    
    # Validate unique Employee ID
    if emp_id in employees:
        print("Employee ID already exists. Please enter a unique ID.")
        return
    
    name = input("Enter Employee Name: ")
    age = int(input("Enter Employee Age: "))
    department = input("Enter Employee Department: ")
    salary = float(input("Enter Employee Salary: "))
    
    # Store the employee data
    employees[emp_id] = {
        'name': name,
        'age': age,
        'department': department,
        'salary': salary
    }
    
    print(f"Employee {name} added successfully.")

def view_employees():
    if not employees:
        print("No employees available.")
        return
    
    print("\n--- Employee List ---")
    print(f"{'ID':<10}{'Name':<20}{'Age':<5}{'Department':<15}{'Salary':<10}")
    print("-" * 60)
    
    for emp_id, details in employees.items():
        print(f"{emp_id:<10}{details['name']:<20}{details['age']:<5}{details['department']:<15}{details['salary']:<10}")

def search_employee():
    emp_id = int(input("Enter Employee ID to search: "))
    
    if emp_id in employees:
        details = employees[emp_id]
        print(f"Employee found: {details['name']}, Age: {details['age']}, Department: {details['department']}, Salary: {details['salary']}")
    else:
        print("Employee not found.")

if __name__ == "__main__":
    main_menu()
