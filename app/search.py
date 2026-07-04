from app.index_manager import product_index


class SearchEngine:
    """
    Product Search using Trie.
    """

    def __init__(self):
        pass

    def search(self, keyword: str):

        if keyword is None:
            return []

        keyword = keyword.strip()

        if keyword == "":
            return []

        return product_index.search(keyword)