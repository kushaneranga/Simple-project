class Employee:
    def __init__(self, names, salary):
        self.names = names
        self.salary = salary

    def print_name(self):
        print(self.names, self.salary)


q = ''
employees = []
while q != 'end':
    q = input("Enter names and salary: ")
    if q == "end":
        break
    n = q.split(',')
    employees.append(Employee(n[0], n[1]))

print("Employees:")
for employee in employees:
    employee.print_name()
