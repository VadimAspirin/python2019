import os
from GUI import InputForm, Menu
from Product import TshirtProduct, SneakersProduct
from Products import Products

CURRENT_FILE_DIR = os.path.dirname(__file__)
ROOT = os.path.dirname(CURRENT_FILE_DIR)
DATA_DIR = os.path.join(ROOT, 'data')
DATA_JSON_PATH = os.path.join(DATA_DIR, 'data.json')

class Program:

    def __init__(self):
        self.products = Products()

    def addTshirt(self):
        # self.products.print()

        input_tshirt = InputForm("Input tshirt:")
        input_tshirt.addItem("sku")
        input_tshirt.addItem("name")
        input_tshirt.addItem("price")
        input_tshirt.addItem("quantity")
        input_tshirt.addItem("brand")
        input_tshirt.addItem("color")
        input_tshirt.addItem("size")
        product_params = input_tshirt.generate()

        product = TshirtProduct(*product_params)
        self.products.add(product)

    def addSneakers(self):
        # self.products.print()

        input_sneakers = InputForm("Input sneakers:")
        input_sneakers.addItem("sku")
        input_sneakers.addItem("name")
        input_sneakers.addItem("price")
        input_sneakers.addItem("quantity")
        input_sneakers.addItem("brand")
        input_sneakers.addItem("color")
        input_sneakers.addItem("size")
        product_params = input_sneakers.generate()

        product = SneakersProduct(*product_params)
        self.products.add(product)

    def delProduct(self):
        input_delete = InputForm("Delete product:")
        input_delete.addItem("sku")
        sku = input_delete.generate()[0]

        self.products.drop(sku)

    def printProduct(self):
        print(f"\n{self.products}")

    def printSizeStat(self):
        print(f"\n{self.products.stat('size')}")

    def printBrandStat(self):
        print(f"\n{self.products.stat('brand')}")

    def run(self):

        self.products.import_from_json(DATA_JSON_PATH)

        product_menu = Menu("Select product type:")
        product_menu.addItem("tshirt", self.addTshirt)
        product_menu.addItem("sneakers", self.addSneakers)
        product_menu.exitItem("back")

        stat_menu = Menu("Select statistic type:")
        stat_menu.addItem("size", self.printSizeStat)
        stat_menu.addItem("brand", self.printBrandStat)
        stat_menu.exitItem("back")

        main_menu = Menu("Select menu item:")
        main_menu.addItem("add product", product_menu.generate)
        main_menu.addItem("print products", self.printProduct)
        main_menu.addItem("del product", self.delProduct)
        main_menu.addItem("print statistics", stat_menu.generate)
        main_menu.exitItem("exit")

        main_menu.generate()

        print('\nBye!')
        self.products.export_to_json(DATA_JSON_PATH)


if __name__ == "__main__":
    Program().run()