class EmployeeData:
    def __init__(self, name: str, department: str) -> None:
        self.name = name
        self.department = department


class PayCalculator:
    def __get_regular_hours(self):
        print("経理部門の仕様変更済み")

    def calculate_pay(self):
        self._get_regular_hours()
        print(f"{self.name}の給与を計算しました")


class HourReporter:
    def __get_regular_hours(self):
        print("人事部門の仕様変更済み")

    def report_hours(self):
        self.get_regular_hours()
        print(f"{self.name}の労働時間をレポートしました")


class EmployeeRepository:
    def save(self):
        print(f"{self.name}を保存しました")


if __name__ == "__main__":
    emp = EmployeeData("山田", "開発")

    print("経理部門")
    emp.calculate_pay()

    print("")
    print("人事部門")
    emp.report_hours()
