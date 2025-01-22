class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"


class EmployeeManager:
    def __init__(self, file_name="employees.txt"):
        self.file_name = file_name

    def _read_file(self):
        try:
            with open(self.file_name, "r") as file:
                return file.readlines()
        except FileNotFoundError:
            return []

    def _write_file(self, lines):
        with open(self.file_name, "w") as file:
            file.writelines(lines)

    def add_employee(self):
        employee = Employee(
            input("Enter Employee ID: "),
            input("Enter Name: "),
            input("Enter Position: "),
            input("Enter Salary: "),
        )
        with open(self.file_name, "a") as file:
            file.write(str(employee) + "\n")
        print("Employee added successfully!")

    def view_employees(self):
        records = self._read_file()
        print("Employee Records:" if records else "No employee records found.")
        for record in records:
            print(record.strip())

    def search_employee(self):
        employee_id = input("Enter Employee ID to search: ")
        for line in self._read_file():
            if line.startswith(employee_id + ","):
                print("Employee Found:", line.strip())
                return
        print("Employee not found.")

    def update_employee(self):
        employee_id = input("Enter Employee ID to update: ")
        updated_records = []
        found = False
        for line in self._read_file():
            if line.startswith(employee_id + ","):
                print("Updating:", line.strip())
                updated_records.append(
                    str(
                        Employee(
                            employee_id,
                            input("Enter new Name: "),
                            input("Enter new Position: "),
                            input("Enter new Salary: "),
                        )
                    )
                    + "\n"
                )
                found = True
            else:
                updated_records.append(line)
        self._write_file(updated_records)
        print("Employee updated successfully!" if found else "Employee not found.")

    def delete_employee(self):
        employee_id = input("Enter Employee ID to delete: ")
        records = self._read_file()
        updated_records = [line for line in records if not line.startswith(employee_id + ",")]
        self._write_file(updated_records)
        print(
            "Employee deleted successfully!" if len(records) != len(updated_records) else "Employee not found."
        )

    def menu(self):
        actions = {
            "1": self.add_employee,
            "2": self.view_employees,
            "3": self.search_employee,
            "4": self.update_employee,
            "5": self.delete_employee,
        }
        while True:
            print(
                "\n1. Add Employee\n2. View Employees\n3. Search Employee\n4. Update Employee\n5. Delete Employee\n6. Exit"
            )
            choice = input("Choose an option: ")
            if choice == "6":
                print("Goodbye!")
                break
            action = actions.get(choice)
            if action:
                action()
            else:
                print("Invalid choice, try again.")


if __name__ == "__main__":
    EmployeeManager().menu()