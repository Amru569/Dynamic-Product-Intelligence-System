class ProductHashMap:
    """
    Fast in-memory lookup for products.

    Supports:
    - Lookup by Product ID
    - Lookup by Product Name
    """

    def __init__(self):

        # Product ID -> Product Object
        self.id_map = {}

        # Product Name -> Product Object
        self.name_map = {}

    def insert(self, product):
        """
        Insert a product into both hash maps.
        """

        # Store by ID
        self.id_map[product.id] = product

        # Store by Name (case-insensitive)
        if product.product_name:

            key = product.product_name.lower().strip()

            self.name_map[key] = product

    def get_by_id(self, product_id):
        """
        O(1) lookup using Product ID.
        """

        return self.id_map.get(product_id)

    def get_by_name(self, product_name):
        """
        O(1) lookup using exact Product Name.
        """

        if not product_name:
            return None

        key = product_name.lower().strip()

        return self.name_map.get(key)

    def contains(self, product_name):
        """
        Check whether a product exists.
        """

        if not product_name:
            return False

        key = product_name.lower().strip()

        return key in self.name_map

    def total_products(self):
        """
        Total products stored.
        """

        return len(self.id_map)

    def get_all_products(self):
        """
        Return all products.
        """

        return list(self.id_map.values())

    def clear(self):
        """
        Remove all products.
        """

        self.id_map.clear()
        self.name_map.clear()