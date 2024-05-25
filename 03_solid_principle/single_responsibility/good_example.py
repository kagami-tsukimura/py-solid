class EmployeeData:
    def __init__(self, name: str, department: str) -> None:
        self.name = name
        self.department = department


class PayCalculator:
    def __get_regular_hours(self):
        print("経理部門の仕様変更済み")

    def calculate_pay(self, employee: EmployeeData):
        self.__get_regular_hours()
        print(f"{employee.name}の給与を計算しました")


class HourReporter:
    def __get_regular_hours(self):
        print("人事部門の仕様変更済み")

    def report_hours(self, employee: EmployeeData):
        self.__get_regular_hours()
        print(f"{employee.name}の労働時間をレポートしました")


class EmployeeRepository:
    def save(self, employee: EmployeeData):
        print(f"{employee.name}を保存しました")


if __name__ == "__main__":
    emp = EmployeeData("山田", "開発")
    calc = PayCalculator()
    rep = HourReporter()

    print("経理部門")
    calc.calculate_pay(emp)

    print("")
    print("人事部門")
    rep.report_hours(emp)
