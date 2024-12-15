class VAT:
    vat_rate = 15  # Class-level attribute

    @staticmethod
    def static_get_vat_price(price):
        return price * (1.0 + VAT.vat_rate / 100)
    def get_vat_price(self, price):
        return price * (1.0 + self.vat_rate / 100)
print(VAT.vat_rate)
print(VAT.static_get_vat_price(50))
vat_instance = VAT()
print(vat_instance.get_vat_price(50))


