class EmployeeData:
    def __init__(self, name: str, department: str) -> None:
        self.name = name
        self.department = department


class PayCalculator:
    def __get_regular_hours(self) -> None:
        print("経理部門ロジック")

    def calculate_pay(self, employee: EmployeeData) -> None:
        self.__get_regular_hours()
        print(f"{employee.name}の給与を計算しました\n")


class HourReporter:
    def __get_regular_hours(self) -> None:
        print("人事部門ロジック")

    def report_hours(self, employee: EmployeeData) -> None:
        self.__get_regular_hours()
        print(f"{employee.name}の労働時間をレポートしました")


class EmployeeRepository:
    def save(self) -> None:
        pass


if __name__ == "__main__":
    emp = EmployeeData("SS", "development")
    calc = PayCalculator()
    rep = HourReporter()

    print("経理部門")
    calc.calculate_pay(emp)

    print("人事部門")
    rep.report_hours(emp)
