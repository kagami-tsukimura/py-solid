from template_method import TestTemplate


class ItemService(TestTemplate):
    def setup(self) -> None:
        print("ItemService.setup")

    def execute(self) -> None:
        print("ItemService.execute")
