from abc import ABCMeta, abstractmethod


class Button(metaclass=ABCMeta):
    @abstractmethod
    def press(self) -> None:
        pass


class Checkbox(metaclass=ABCMeta):
    @abstractmethod
    def switch(self) -> None:
        pass


class GUIFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


class WindowsButton(Button):
    def press(self) -> None:
        print("WindowsButton is pressed")


class WindowsCheckbox(Checkbox):
    def switch(self) -> None:
        print("WindowsCheckbox is switched")


class WindowsGUIFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()


if __name__ == "__main__":
    factory = WindowsGUIFactory()
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    button.press()
    checkbox.switch()
