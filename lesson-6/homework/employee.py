def add_employee():
    with open("employees.txt", "a") as file:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        position = input("Enter Employee Position: ")
        salary = input("Enter Employee Salary: ")
        file.write(f"{emp_id},{name},{position},{salary}\n")
    print("Employee added.\n")

def view_employees():
    try:
        with open("employees.txt", "r") as file:
            print("\nEmployee Records:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No records found.\n")

def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    try:
        with open("employees.txt", "r") as file:
            for line in file:
                if line.startswith(emp_id + ","):
                    print("Record found:", line.strip())
                    return
        print("No employee found with that ID.\n")
    except FileNotFoundError:
        print("No records found.\n")

def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    try:
        updated = False
        with open("employees.txt", "r") as file:
            lines = file.readlines()
        with open("employees.txt", "w") as file:
            for line in lines:
                if line.startswith(emp_id + ","):
                    updated = True
                    print("Current Record:", line.strip())
                    name = input("Enter new name (or press Enter to keep): ")
                    position = input("Enter new position (or press Enter to keep): ")
                    salary = input("Enter new salary (or press Enter to keep): ")
                    fields = line.strip().split(",")
                    file.write(f"{emp_id},{name or fields[1]},{position or fields[2]},{salary or fields[3]}\n")
                else:
                    file.write(line)
        print("Employee updated.\n" if updated else "Employee not found.\n")
    except FileNotFoundError:
        print("No records found.\n")

def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    try:
        deleted = False
        with open("employees.txt", "r") as file:
            lines = file.readlines()
        with open("employees.txt", "w") as file:
            for line in lines:
                if line.startswith(emp_id + ","):
                    deleted = True
                else:
                    file.write(line)
        print("Employee deleted.\n" if deleted else "Employee not found.\n")
    except FileNotFoundError:
        print("No records found.\n")

def main():
    while True:
        print("\nMenu:")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()