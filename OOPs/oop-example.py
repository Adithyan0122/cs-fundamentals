from abc import ABC, abstractmethod

# 1. ABSTRACTION: Creating a blueprint that cannot be instantiated directly.
class Employee(ABC):
    def __init__(self, name, employee_id):
        self.name = name
        # 2. ENCAPSULATION: Hiding the ID variable with a double underscore.
        self.__employee_id = employee_id  

    # ENCAPSULATION: Using a getter method to safely access the private variable.
    def get_employee_id(self):
        return self.__employee_id

    # ABSTRACTION: Forcing all child classes to create their own version of this method.
    @abstractmethod
    def calculate_salary(self):
        pass

# 3. INHERITANCE: FullTimeEmployee inherits properties and methods from Employee.
class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, annual_salary):
        super().__init__(name, employee_id) # Calling the parent constructor
        self.__annual_salary = annual_salary

    # 4. POLYMORPHISM: Implementing the specific salary logic for a full-time worker.
    def calculate_salary(self):
        return self.__annual_salary / 12

# 3. INHERITANCE: Contractor also inherits from Employee.
class Contractor(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        super().__init__(name, employee_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    # 4. POLYMORPHISM: Implementing entirely different salary logic for a contractor.
    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

# --- Execution ---

# Creating Objects (Instances)
alice = FullTimeEmployee("Alice Smith", "FT-001", 120000)
bob = Contractor("Bob Jones", "CT-999", 50, 160)

# POLYMORPHISM IN ACTION: 
# This function accepts a list of generic 'Employees'. It does not need to know 
# if they are contractors or full-time. It just calls calculate_salary() and 
# trusts the objects to handle their own specific math.
def process_payroll(staff_list):
    for staff in staff_list:
        emp_id = staff.get_employee_id()
        salary = staff.calculate_salary()
        print(f"Payroll for {staff.name} (ID: {emp_id}): ${salary:,.2f}")

# Running the system
company_staff = [alice, bob]
process_payroll(company_staff)
