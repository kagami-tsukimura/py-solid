# クラス図の実装
class Employee:
    def __init__(self, emp_id: int, name: str, salary: int):
        self.__emp_id = emp_id
        self.__name = name
        self.__salary = salary

    def _work(self) -> None:
        print(f"{self.__name} is working")

    # # getter, setter
    # def get_saraly(self) -> int:
    #     return self.__salary

    # def set_salary(self, salary: int) -> None:
    #     self.__salary = salary

    # property decorator
    @property
    def salary(self) -> str:
        return self.__salary

    @salary.setter
    def salary(self, salary: int) -> None:
        self.__salary = salary
