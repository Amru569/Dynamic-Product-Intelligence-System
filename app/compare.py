from app.index_manager import product_index


class PriceComparisonEngine:
    """
    Price Intelligence Engine.
    """

    def __init__(self):
        pass

    def cheapest_product(self):

        return product_index.cheapest_product()

    def top_cheapest(self, limit=10):

        return product_index.cheapest_products(limit)