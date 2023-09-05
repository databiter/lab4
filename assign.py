class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"Employee ID: {self.emp_id}, Name: {self.name}, Age: {self.age}, Salary: {self.salary}"

class EmployeeTable:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def search_by_age(self, age):
        result = [emp for emp in self.employees if emp.age == age]
        return result

    def search_by_name(self, name):
        result = [emp for emp in self.employees if emp.name.lower() == name.lower()]
        return result

    def search_by_salary(self, operator, salary):
        operators = {
            ">": lambda x, y: x > y,
            "<": lambda x, y: x < y,
            ">=": lambda x, y: x >= y,
            "<=": lambda x, y: x <= y
        }
        if operator not in operators:
            return []

        result = [emp for emp in self.employees if operators[operator](emp.salary, salary)]
        return result

    def display(self, employees):
        for emp in employees:
            print(emp)

def main():
    table = EmployeeTable()

    # Add sample employees to the table
    table.add_employee(Employee("161E90", "Raman", 41, 56000))
    table.add_employee(Employee("161F91", "Himadri", 38, 67500))
    table.add_employee(Employee("161F99", "Jaya", 51, 82100))
    table.add_employee(Employee("171E20", "Tejas", 30, 55000))
    table.add_employee(Employee("171G30", "Ajay", 45, 44000))

    print("Choose a search parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary (>, <, <=, >=)")
    choice = input("Enter your choice: ")

    if choice == "1":
        age = int(input("Enter age to search: "))
        result = table.search_by_age(age)
    elif choice == "2":
        name = input("Enter name to search: ")
        result = table.search_by_name(name)
    elif choice == "3":
        operator = input("Enter operator (>, <, <=, >=): ")
        salary = float(input("Enter salary to compare: "))
        result = table.search_by_salary(operator, salary)
    else:
        print("Invalid choice")
        return

    if result:
        print("Search Results:")
        table.display(result)
    else:
        print("No matching records found")

if __name__ == "__main__":
    main()
