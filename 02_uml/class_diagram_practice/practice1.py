# クラス図の実装
class Employee:
    def __init__(self, emp_id: int, name: str, salary: int):
        self.__emp_id = emp_id
        self.__name = name
        self.__salary = salary

    def _work(self) -> None:
        print(f"{self.name} is working")

    def get_saraly(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary
