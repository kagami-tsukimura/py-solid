# クラス図の実装
class Employee:
    def __init__(self, id, name, salary):
        self.emp_id: int = id
        self.name: str = name
        self.salary: int = salary

    def _work(self):
        print(f"{self.name} is working")

    def get_saraly(self):
        return self.salary

    def set_salary(self, salary):
        self.salary = salary
