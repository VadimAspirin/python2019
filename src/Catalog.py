import os
import json
from Product import Product, ProductCreator


class Catalog:
    def __init__(self):
        self.products = {}

    def __getitem__(self, item):
         return self.products[item]

    def __str__(self):
        if not self.products:
            return ""

        out = "--------------\n"
        for i in self.products:
            out += self.to_string(i)
            out += "--------------\n"
        return out

    def add(self, product):
        assert isinstance(product, Product), "product is not type Product"
        self.products[product.sku] = product

    def drop(self, sku):
        if sku not in self.products:
            raise ValueError("product not found")
        del self.products[sku]
            
    def to_string(self, sku):
        if sku not in self.products:
            raise ValueError("product not found")
        out = f"type: {type(self.products[sku]).type_name}\n"
        out += self.products[sku].__str__()
        return out

    def filter_collect(self, **kwargs):
        ids = []
        for i in self.products:
            f = 0
            for j in kwargs:
                if not hasattr(self.products[i], j):
                    break
                elif str(f"{eval(f'self.products[i].{j}')}") != kwargs[j]:
                    break
                f += 1
            if f == len(kwargs):
                ids.append(i)
        return ids

    def filter(self, **kwargs):
        ids = self.filter_collect(**kwargs)
        if not ids:
            return ""

        out = "--------------\n"
        for i in ids:
            out += self.to_string(i)
            out += "--------------\n"
        return out

    def stat_collect(self, param):
        out = {}
        for i in self.products:
            if param not in self.products[i].params:
                continue

            name = self.products[i][param]
            if name in out:
                out[name] += 1
            else:
                out[name] = 1
        return out

    def stat(self, param):
        if not self.products:
            return ""

        out = f"Statistics for {param}\n<item>: <count>\n"
        stat_info = self.stat_collect(param)
        for name, count in stat_info.items():
            out += f"{name}: {count}\n"
        return out


class CatlogFileLoader:

    def __init__(self, path):
        self.path = path

    def input(self, catalog):
        assert isinstance(catalog, Catalog)

        if not os.path.isfile(self.path):
            return

        data = []
        with open(self.path, 'r') as fp:
            data = json.load(fp)

        catalog.products = {}
        for p in data:
            product = ProductCreator.pull(p['type'], p['params'])
            catalog.products[product.params['sku']] = product

    def output(self, catalog):
        assert isinstance(catalog, Catalog)

        if not catalog.products:
            return

        data = []
        for _, p in catalog.products.items():
            data.append({"type": type(p).__name__, 
                         "params": p.params})

        with open(self.path, 'w') as fp:
            json.dump(data, fp)