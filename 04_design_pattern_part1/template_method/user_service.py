from template_method import TestTemplate


class UserService(TestTemplate):
    def setup(self) -> None:
        print("UserService.setup")

    def execute(self) -> None:
        print("UserService.execute")
