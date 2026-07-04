import heapq


class MinHeap:
    """
    Min Heap for Product Prices.
    """

    def __init__(self):
        self.heap = []

    def build(self, products):

        self.heap = []

        for product in products:

            heapq.heappush(

                self.heap,

                (

                    float(product.price),

                    product.id,

                    product.product_name

                )

            )

    def get_cheapest(self):

        if not self.heap:

            return None

        return self.heap[0]

    def get_top_cheapest(self, limit=10):

        return heapq.nsmallest(limit, self.heap)

    def size(self):

        return len(self.heap)

    def clear(self):

        self.heap.clear()