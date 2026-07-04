from app.index_manager import product_index


class ProductLookup:
    """
    Product Lookup using HashMap.
    """

    def __init__(self):
        pass

    def get_product(self, product_name: str):

        if product_name is None:
            return None

        product_name = product_name.strip()

        if product_name == "":
            return None

        return product_index.get_product(product_name)

    def get_product_by_id(self, product_id: int):

        return product_index.get_product_by_id(product_id)