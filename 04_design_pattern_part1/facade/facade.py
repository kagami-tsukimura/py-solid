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
    def __init__(self, product: Product, payment: Payment, invoice: Invoice):
        self.product = product
        self.payment = payment
        self.invoice = invoice

    def make_order(self, name: str):
        self.product.get_product(name)
        self.payment.make_payment(name)
        self.invoice.send_invoice(name)
