class Discount:
    default_discount = 5

    @classmethod
    def show_discount(cls):
        print(f"Default discount: {cls.default_discount}%")

    @staticmethod
    def ask_discount():
        return int(input("Enter special discount %: "))


class Shipping:
    base_fee = 50

    @staticmethod
    def ask_shipping_weight():
        return float(input("Enter package weight (kg): "))

    @classmethod
    def show_base_fee(cls):
        print(f"Base shipping fee: {cls.base_fee}")


class Order(Discount, Shipping):
    company_name = "ShopEase"

    def __init__(self, order_id, item_price):
        self.order_id = order_id
        self.item_price = item_price

    def order_details(self):
        print(f"Company: {self.company_name}")
        print(f"Order ID: {self.order_id}")
        print(f"Item Price: {self.item_price}")

    def calculate_total(self):
        discounted = self.item_price * (100 - self.default_discount) / 100
        extra = self.ask_discount()
        discounted *= (100 - extra) / 100
        weight = self.ask_shipping_weight()
        shipping = self.base_fee + weight * 10
        total = discounted + shipping
        print(f"Total payable: {total}")


o = Order("ORD123", 2000)
o.order_details()
Order.show_discount()
Order.show_base_fee()
o.calculate_total()
