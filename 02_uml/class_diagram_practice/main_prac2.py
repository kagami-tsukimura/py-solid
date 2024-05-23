from practice2 import Employee

if __name__ == "__main__":
    employee = Employee(1, "John", 10000)
    employee._work()
    print(employee.salary)
    employee.salary = 20000
    print(employee.salary)
