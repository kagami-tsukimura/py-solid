class Product:
    def get_product(self, name: str):
        print(f"{name}を取得しました。")


class Payment:
    def make_payment(self, name: str):
        print(f"{name}を支払いました。")


class Invoice:
    def send_invoice(self, name: str):
        print(f"{name}の請求書を送信しました。")


class Order:
    def place_order(self, name: str):
        print("注文開始")
        product = Product()
        product.get_product(name)
        payment = Payment()
        payment.make_payment(name)
        invoice = Invoice()
        invoice.send_invoice(name)
        print("注文完了")


if __name__ == "__main__":
    name1 = "design pattern"
    order = Order()
    order.place_order(name1)

    print("-----")

    name2 = "デザインパターン"
    order.place_order(name2)
