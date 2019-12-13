import pytest
import os
import sys

CURRENT_FILE_DIR = os.path.dirname(__file__)
ROOT = os.path.dirname(CURRENT_FILE_DIR)
SRC_DIR = os.path.join(ROOT, 'src')
DATA_JSON_PATH = os.path.join(CURRENT_FILE_DIR, 'test.json')

sys.path.append(SRC_DIR)


from Products import Products
from Product import TshirtProduct

sku=1
name="noname1"
price=42
quantity=2
brand="noname"
color="red"
size="M"


def test_export_import_products():
    product = TshirtProduct(sku, name, price, quantity, brand, color, size)
    products = Products()
    products.add(product)
    products.export_to_json(DATA_JSON_PATH)

    new_products = Products()
    new_products.import_from_json(DATA_JSON_PATH)

    assert new_products.products[0].params['sku'] == products.products[0].params['sku'] == sku
    assert new_products.products[0].params['name'] == products.products[0].params['name'] == name
    assert new_products.products[0].params['price'] == products.products[0].params['price'] == price
    assert new_products.products[0].params['quantity'] == products.products[0].params['quantity'] == quantity
    assert new_products.products[0].params['brand'] == products.products[0].params['brand'] == brand
    assert new_products.products[0].params['color'] == products.products[0].params['color'] == color
    assert new_products.products[0].params['size'] == products.products[0].params['size'] == size


def test_add_product():
    product = TshirtProduct(sku, name, price, quantity, brand, color, size)
    products = Products()
    products.add(product)

    assert products.products[0].params['sku'] == sku
    assert products.products[0].params['name'] == name
    assert products.products[0].params['price'] == price
    assert products.products[0].params['quantity'] == quantity
    assert products.products[0].params['brand'] == brand
    assert products.products[0].params['color'] == color
    assert products.products[0].params['size'] == size


def test_empty_product():
    with pytest.raises(Exception) as e_info:
        TshirtProduct()

    with pytest.raises(Exception) as e_info:
        TshirtProduct("", "", "", "", "", "", "")

    with pytest.raises(Exception) as e_info:
        TshirtProduct(sku, name, "test", "test", brand, color, size)


def test_update_product():
    products = Products()
    product = TshirtProduct(sku, name, price, quantity, brand, color, size)
    products.add(product)

    new_name="noname2"
    new_price=46
    new_quantity=6
    new_brand="noname_noname"
    new_color="black"
    new_size="S"

    product = TshirtProduct(sku, new_name, new_price, new_quantity, new_brand, new_color, new_size)
    products.add(product)

    assert products.products[0].params['sku'] == sku
    assert products.products[0].params['name'] == new_name
    assert products.products[0].params['price'] == new_price
    assert products.products[0].params['quantity'] == new_quantity
    assert products.products[0].params['brand'] == new_brand
    assert products.products[0].params['color'] == new_color
    assert products.products[0].params['size'] == new_size


def test_delete_product():
    products = Products()
    product = TshirtProduct(sku, name, price, quantity, brand, color, size)
    products.add(product)
    assert len(products.products) == 1

    products.drop(sku)
    assert len(products.products) == 0


def test_stat_size_product():
    products = Products()
    products.add(TshirtProduct(sku, name, price, quantity, brand, color, "L"))
    products.add(TshirtProduct(sku+1, name, price, quantity, brand, color, "S"))
    products.add(TshirtProduct(sku+2, name, price, quantity, brand, color, "S"))
    products.add(TshirtProduct(sku+3, name, price, quantity, brand, color, "M"))
    products.add(TshirtProduct(sku+4, name, price, quantity, brand, color, "M"))
    products.add(TshirtProduct(sku+5, name, price, quantity, brand, color, "M"))
    products.add(TshirtProduct(sku+6, name, price, quantity, brand, color, "XXXL"))

    stat_size = products._collect_stat("size")
    assert stat_size["L"] == 1
    assert stat_size["S"] == 2
    assert stat_size["M"] == 3
    assert stat_size["XXXL"] == 1


def test_negative_price_product():
    with pytest.raises(Exception) as e_info:
        TshirtProduct(sku, name, -100, quantity, brand, color, size)
    
    with pytest.raises(Exception) as e_info:
        TshirtProduct(sku, name, -1, quantity, brand, color, size)