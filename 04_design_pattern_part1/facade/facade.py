class Product:
    def get_product(self, name: str):
        print(f"{name}を取得しました。")


class Payment:
    def make_payment(self, name: str):
        print(f"{name}を支払いました。")


class Invoice:
    def send_invoice(self, name: str):
        print(f"{name}の請求書を送信しました。")
