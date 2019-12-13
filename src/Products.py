import os
import json
from Product import Product, ProductCreator

class Products:
    def __init__(self):
        self.products = []

    def search(self, sku):
        current_prod = None
        for i in range(len(self.products)):
            if str(self.products[i].params['sku']) == str(sku):
                return i
        return None

    def add(self, product):
        assert isinstance(product, Product), "product is not type Product"

        current_prod = self.search(product.params['sku'])
        if current_prod is not None:
            self.products[current_prod] = product
        else:
            self.products.append(product)

    def drop(self, sku):
        current_prod = self.search(sku)
        if current_prod is not None:
            del self.products[current_prod]
        else:
            raise ValueError("product not found")

    def __str__(self):
        out = ""
        if not self.products:
            return out

        out += "--------------\n"
        for p in self.products:
            out += f"type: {p.type_name}\n"
            out += p.__str__()
            out += "--------------\n"
        return out

    def _collect_stat(self, param):
        out = {}
        for i in range(len(self.products)):
            if param not in self.products[i].params:
                continue

            name = self.products[i].params[param]
            if name in out:
                out[name] += 1
            else:
                out[name] = 1
        return out

    def stat(self, param):
        stat = ""
        if not self.products:
            return stat

        stat += f"Statistics for {param}\n<item>: <count>\n"
        stat_info = self._collect_stat(param)
        for name, count in stat_info.items():
            stat += f"{name}: {count}\n"
        return stat

    def import_from_json(self, path):
        if not os.path.isfile(path):
            return

        data = []
        with open(path, 'r') as fp:
            data = json.load(fp)

        self.products = []
        for p in data:
            product = ProductCreator.pull(p['type'], p['params'])
            self.products.append(product)

    def export_to_json(self, path):
        if not self.products:
            return

        data = []
        for p in self.products:
            data.append({"type": p.type_name, 
                         "params": p.params})

        with open(path, 'w') as fp:
            json.dump(data, fp)