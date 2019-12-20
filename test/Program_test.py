import pytest
import os
import sys

CURRENT_FILE_DIR = os.path.dirname(__file__)
ROOT = os.path.dirname(CURRENT_FILE_DIR)
SRC_DIR = os.path.join(ROOT, 'src')
DATA_JSON_PATH = os.path.join(CURRENT_FILE_DIR, 'test.json')

sys.path.append(SRC_DIR)


from Catalog import Catalog
from Product import TshirtProduct, SneakersProduct

sku=1
name="noname1"
price=42
quantity=2
brand="noname"
color="red"
size="M"


def test_parser():
    tshirt = TshirtProduct("1", "name1", 42, 2, "noname", "blue", "S")
    sneakers = SneakersProduct("2", "nike-mew", 777.45, 12, "nike", "black", 41)
    catalog = Catalog()
    catalog.add(tshirt)
    catalog.add(sneakers)
    catalog.export_to_json(DATA_JSON_PATH)

    new_catalog = Catalog()
    new_catalog.import_from_json(DATA_JSON_PATH)

    assert type(new_catalog[tshirt.sku]).__name__ == 'TshirtProduct'
    assert type(new_catalog[sneakers.sku]).__name__ == 'SneakersProduct'


def test_export_import_products():
    product = TshirtProduct(sku, name, price, quantity, brand, color, size)
    catalog = Catalog()
    catalog.add(product)
    catalog.export_to_json(DATA_JSON_PATH)

    new_catalog = Catalog()
    new_catalog.import_from_json(DATA_JSON_PATH)

    assert new_catalog[sku].sku == catalog[sku].sku == sku
    assert new_catalog[sku].name == catalog[sku].name == name
    assert new_catalog[sku].price == catalog[sku].price == price
    assert new_catalog[sku].quantity == catalog[sku].quantity == quantity
    assert new_catalog[sku].brand == catalog[sku].brand == brand
    assert new_catalog[sku].color == catalog[sku].color == color
    assert new_catalog[sku].size == catalog[sku].size == size


def test_add_product():
    product = TshirtProduct(sku, name, price, quantity, brand, color, size)
    catalog = Catalog()
    catalog.add(product)

    assert catalog[sku].sku == sku
    assert catalog[sku].name == name
    assert catalog[sku].price == price
    assert catalog[sku].quantity == quantity
    assert catalog[sku].brand == brand
    assert catalog[sku].color == color
    assert catalog[sku].size == size


def test_empty_product():
    with pytest.raises(Exception) as e_info:
        TshirtProduct()

    with pytest.raises(Exception) as e_info:
        TshirtProduct("", "", "", "", "", "", "")

    with pytest.raises(Exception) as e_info:
        TshirtProduct(sku, name, "test", "test", brand, color, size)


def test_update_product():
    catalog = Catalog()
    product = TshirtProduct(sku, name, price, quantity, brand, color, size)
    catalog.add(product)

    new_name="noname2"
    new_price=46
    new_quantity=6
    new_brand="noname_noname"
    new_color="black"
    new_size="S"

    product = TshirtProduct(sku, new_name, new_price, new_quantity, new_brand, new_color, new_size)
    catalog.add(product)

    assert catalog[sku].sku == sku
    assert catalog[sku].name == new_name
    assert catalog[sku].price == new_price
    assert catalog[sku].quantity == new_quantity
    assert catalog[sku].brand == new_brand
    assert catalog[sku].color == new_color
    assert catalog[sku].size == new_size


def test_delete_product():
    catalog = Catalog()
    product = TshirtProduct(sku, name, price, quantity, brand, color, size)
    catalog.add(product)
    assert len(catalog.products) == 1

    catalog.drop(sku)
    assert len(catalog.products) == 0


def test_stat_size_product():
    catalog = Catalog()
    catalog.add(TshirtProduct(sku, name, price, quantity, brand, color, "L"))
    catalog.add(TshirtProduct(sku+1, name, price, quantity, brand, color, "S"))
    catalog.add(TshirtProduct(sku+2, name, price, quantity, brand, color, "S"))
    catalog.add(TshirtProduct(sku+3, name, price, quantity, brand, color, "M"))
    catalog.add(TshirtProduct(sku+4, name, price, quantity, brand, color, "M"))
    catalog.add(TshirtProduct(sku+5, name, price, quantity, brand, color, "M"))
    catalog.add(TshirtProduct(sku+6, name, price, quantity, brand, color, "XXXL"))

    stat_size = catalog.stat_collect("size")
    assert stat_size["L"] == 1
    assert stat_size["S"] == 2
    assert stat_size["M"] == 3
    assert stat_size["XXXL"] == 1


def test_negative_price_product():
    with pytest.raises(Exception) as e_info:
        TshirtProduct(sku, name, -100, quantity, brand, color, size)
    
    with pytest.raises(Exception) as e_info:
        TshirtProduct(sku, name, -1, quantity, brand, color, size)