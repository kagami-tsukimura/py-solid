from abc import ABCMeta, abstractmethod


class Employee(metaclass=ABCMeta):
    def __init__(self, name: str, department: str) -> None:
        self.name = name
        self.department = department

    @abstractmethod
    def get_regular_hours(self) -> None:
        pass


class Calculator(Employee):
    # 経理部門がアクター
    def get_regular_hours(self) -> None:
        print("経理部門の仕様変更済み")

    def calculate_pay(self) -> None:
        self.get_regular_hours()
        print(f"{self.name}の給与を計算しました")


class Reporter(Employee):
    # 人事部門がアクター
    def get_regular_hours(self) -> None:
        print("人事部門の仕様変更済み")

    def report_hours(self) -> None:
        self.get_regular_hours()
        print(f"{self.name}の労働時間をレポートしました")


class Engineer(Employee):
    # エンジニアがアクター
    def save(self) -> None:
        print(f"{self.name}を保存しました")


if __name__ == "__main__":
    emp = Employee("山田", "開発")
    calc = Calculator(Employee)
    rep = Reporter(Employee)
    eng = Engineer(Employee)

    print("経理部門")
    calc.calculate_pay()

    print("")
    print("人事部門")
    rep.report_hours()
