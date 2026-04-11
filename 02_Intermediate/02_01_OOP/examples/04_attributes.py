class Employee:
    # Class Attribute (shared by all employees)
    company = "xAI"
    employee_count = 0
   
    def __init__(self, name, salary):
        # Instance Attributes (unique to each employee)
        self.name = name
        self.salary = salary
        self.department = "Engineering"
       
        Employee.employee_count += 1   # Accessing class attribute
   
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Salary: ₹{self.salary}")
        print(f"Company: {self.company}")   # Accessing class attribute
# Creating objects
e1 = Employee("Sunny", 120000)
e2 = Employee("Priya", 95000)
e1.show_details()
e2.show_details()
print(f"\nTotal Employees: {Employee.employee_count}")
print(f"Company: {Employee.company}")
