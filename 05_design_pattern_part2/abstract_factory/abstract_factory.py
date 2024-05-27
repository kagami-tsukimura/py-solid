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


class MacButton(Button):
    def press(self) -> None:
        print("MacButton is pressed")


class MacCheckbox(Checkbox):
    def switch(self) -> None:
        print("MacCheckbox is switched")


class MacGUIFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()


if __name__ == "__main__":
    windows_factory = WindowsGUIFactory()
    windows_button = windows_factory.create_button()
    windows_checkbox = windows_factory.create_checkbox()
    windows_button.press()
    windows_checkbox.switch()

    mac_factory = MacGUIFactory()
    mac_button = mac_factory.create_button()
    mac_checkbox = mac_factory.create_checkbox()
    mac_button.press()
    mac_checkbox.switch()
