import inspect
from Catalog import Catalog
from Product import Products
from UI import InputForm, Menu


class UICatalog:

    class UIProduct:
        def __init__(self, ui_catalog_instance, product_class):
            self.ui_catalog_instance = ui_catalog_instance
            self.product_class = product_class
            self.type_name = product_class.type_name
            self.fields = inspect.getfullargspec(product_class.__init__)[0][1:]

        def input(self, empty_input=False):
            input_product = InputForm(f"Input {self.type_name}: ", empty_input)
            for i in self.fields:
                input_product.addItem(i)
            return input_product.generate()

        def add(self):
            product_params = self.input()
            self.ui_catalog_instance.catalog.add(self.product_class(*product_params))

        def filter(self):
            product_params = self.input(True)
            params = dict(zip(self.fields, product_params))
            params = {k: v for k, v in params.items() if v}
            print(f"\n{self.ui_catalog_instance.catalog.filter(type_name=self.type_name, **params)}")


    def _UIProduct(self, product_class):
        return UICatalog.UIProduct(self, product_class)

    def __init__(self, data_json_path):
        self.ui_products = []
        for procuct_class in Products.list():
            self.ui_products.append(self._UIProduct(procuct_class))
        self.catalog = Catalog()
        self.data_json_path = data_json_path

    def addProduct(self):
        product_menu = Menu("Select product type:")
        for ui_product in self.ui_products:
            product_menu.addItem(ui_product.type_name, ui_product.add)
        product_menu.exitItem("back")
        product_menu.generate()

    def delProduct(self):
        input_delete = InputForm("Delete product:")
        input_delete.addItem("sku")
        sku = input_delete.generate()[0]
        self.catalog.drop(sku)

    def printProduct(self):
        print(f"\n{self.catalog}")

    def _printSizeStat(self):
        print(f"\n{self.catalog.stat('size')}")

    def _printBrandStat(self):
        print(f"\n{self.catalog.stat('brand')}")

    def printStatistic(self):
        stat_menu = Menu("Select statistic type:")
        stat_menu.addItem("size", self._printSizeStat)
        stat_menu.addItem("brand", self._printBrandStat)
        stat_menu.exitItem("back")
        stat_menu.generate()

    def filterProduct(self):
        filter_product_menu = Menu("Select product type:")
        for ui_product in self.ui_products:
            filter_product_menu.addItem(ui_product.type_name, ui_product.filter)
        filter_product_menu.exitItem("back")
        filter_product_menu.generate()

    def generate(self):
        self.catalog.import_from_json(self.data_json_path)

        main_menu = Menu("Select menu item:")
        main_menu.addItem("add product", self.addProduct)
        main_menu.addItem("print products", self.printProduct)
        main_menu.addItem("del product", self.delProduct)
        main_menu.addItem("statistics", self.printStatistic)
        main_menu.addItem("filter", self.filterProduct)
        main_menu.exitItem("exit")
        main_menu.generate()

        print('\nBye!')
        self.catalog.export_to_json(self.data_json_path)