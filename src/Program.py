import os
import inspect
from UI import InputForm, Menu
from Product import TshirtProduct, SneakersProduct
from Catalog import Catalog

CURRENT_FILE_DIR = os.path.dirname(__file__)
ROOT = os.path.dirname(CURRENT_FILE_DIR)
DATA_DIR = os.path.join(ROOT, 'data')
DATA_JSON_PATH = os.path.join(DATA_DIR, 'data.json')

class Program:

    def __init__(self):
        self.catalog = Catalog()
        self.tshirt_params = inspect.getfullargspec(TshirtProduct.__init__)[0]
        self.tshirt_params.remove('self')
        self.sneakers_params = inspect.getfullargspec(SneakersProduct.__init__)[0]
        self.sneakers_params.remove('self')

    def inputProduct(self, name, fields, empty_input=False):
        input_product = InputForm(f"Input {name}: ", empty_input)
        for i in fields:
            input_product.addItem(i)
        return input_product.generate()

    def addTshirt(self):
        product_params = self.inputProduct('tshirt', self.tshirt_params)
        product = TshirtProduct(*product_params)
        self.catalog.add(product)

    def addSneakers(self):
        product_params = self.inputProduct('sneakers', self.sneakers_params)
        product = SneakersProduct(*product_params)
        self.catalog.add(product)

    def delProduct(self):
        input_delete = InputForm("Delete product:")
        input_delete.addItem("sku")
        sku = input_delete.generate()[0]
        self.catalog.drop(sku)

    def printProduct(self):
        print(f"\n{self.catalog}")

    def printSizeStat(self):
        print(f"\n{self.catalog.stat('size')}")

    def printBrandStat(self):
        print(f"\n{self.catalog.stat('brand')}")

    def filterTshirt(self):
        product_params = self.inputProduct('tshirt', self.tshirt_params, True)
        params = dict(zip(self.tshirt_params, product_params))
        print(f"\n{self.catalog.filter(type_name='Tshirt', **params)}")

    def filterSneakers(self):
        product_params = self.inputProduct('sneakers', self.sneakers_params, True)
        params = dict(zip(self.sneakers_params, product_params))
        print(f"\n{self.catalog.filter(type_name='Sneakers', **params)}")

    def run(self):

        self.catalog.import_from_json(DATA_JSON_PATH)

        add_product_menu = Menu("Select product type:")
        add_product_menu.addItem("tshirt", self.addTshirt)
        add_product_menu.addItem("sneakers", self.addSneakers)
        add_product_menu.exitItem("back")

        filter_product_menu = Menu("Select product type:")
        filter_product_menu.addItem("tshirt", self.filterTshirt)
        filter_product_menu.addItem("sneakers", self.filterSneakers)
        filter_product_menu.exitItem("back")

        stat_menu = Menu("Select statistic type:")
        stat_menu.addItem("size", self.printSizeStat)
        stat_menu.addItem("brand", self.printBrandStat)
        stat_menu.exitItem("back")

        main_menu = Menu("Select menu item:")
        main_menu.addItem("add product", add_product_menu.generate)
        main_menu.addItem("print products", self.printProduct)
        main_menu.addItem("del product", self.delProduct)
        main_menu.addItem("print statistics", stat_menu.generate)
        main_menu.addItem("filter", filter_product_menu.generate)
        main_menu.exitItem("exit")

        main_menu.generate()

        print('\nBye!')
        self.catalog.export_to_json(DATA_JSON_PATH)


if __name__ == "__main__":
    Program().run()