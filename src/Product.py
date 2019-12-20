class Product:
    def __init__(self, sku, name, price, quantity, brand):
        self.type_name = "Product"
        self.params = {}
        self.params['sku'] = sku
        self.params['name'] = name
        self.params['price'] = float(price)
        self.params['quantity'] = int(quantity)
        self.params['brand'] = brand

        if self.params['price'] < 0:
            raise ValueError("price < 0")

        if self.params['quantity'] < 0:
            raise ValueError("quantity < 0")

        for k, v in self.params.items():
            if not v:
                raise ValueError(f"{k} is empty")

    def __getitem__(self, item):
         return self.params[item]

    def __getattr__(self, item):
        return self.params[item]

    def __str__(self):
        out = ""
        for k, v in self.params.items():
           out += f'{k}: {v}\n'
        return out


class TshirtProduct(Product):
    def __init__(self, sku, name, price, quantity, brand, color, size):
        super(TshirtProduct, self).__init__(sku, name, price, quantity, brand)
        self.type_name = "Tshirt"
        self.params['color'] = color
        self.params['size'] = size

        for k, v in self.params.items():
            if not v:
                raise ValueError(f"{k} is empty")

        sizes = ['S', 'M', 'L', 'XL', 'XXL', 'XXXL']
        if self.params['size'] not in sizes:
            raise ValueError(f"size is not: {sizes}")


class SneakersProduct(Product):
    def __init__(self, sku, name, price, quantity, brand, color, size):
        super(SneakersProduct, self).__init__(sku, name, price, quantity, brand)
        self.type_name = "Sneakers"
        self.params['color'] = color
        self.params['size'] = int(size)

        for k, v in self.params.items():
            if not v:
                raise ValueError(f"{k} is empty")


class ProductCreator:
    @staticmethod
    def pull(p_type, params):
        return eval(f'{p_type}(**params)')