from app.trie import Trie
from app.hashmap import ProductHashMap
from app.heap import MinHeap


class ProductIndex:
    """
    Central in-memory index for products.

    Maintains:
    1. Trie      -> Prefix Search
    2. HashMap   -> O(1) Lookup
    3. MinHeap   -> Cheapest Products
    """

    def __init__(self):

        self.trie = Trie()

        self.hashmap = ProductHashMap()

        self.heap = MinHeap()

        self.total_products = 0

    def build(self, products):

        # Reset indexes

        self.trie = Trie()

        self.hashmap = ProductHashMap()

        self.heap = MinHeap()

        self.total_products = 0

        for product in products:

            if not product.product_name:
                continue

            # Build Trie

            self.trie.insert(product.product_name)

            # Build HashMap

            self.hashmap.insert(product)

            self.total_products += 1

        # Build Heap once

        self.heap.build(products)

    # =====================================
    # Trie
    # =====================================

    def search(self, keyword):

        return self.trie.search_prefix(keyword)

    # =====================================
    # HashMap
    # =====================================

    def get_product(self, product_name):

        return self.hashmap.get_by_name(product_name)

    def get_product_by_id(self, product_id):

        return self.hashmap.get_by_id(product_id)

    # =====================================
    # Heap
    # =====================================

    def cheapest_product(self):

        return self.heap.get_cheapest()

    def cheapest_products(self, limit=10):

        return self.heap.get_top_cheapest(limit)