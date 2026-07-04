import re
import pandas as pd


class ColumnMapper:
    """
    Dynamically maps uploaded CSV columns
    to the platform's internal schema.
    """

    COLUMN_MAPPING = {

        "product_name": [
            "product",
            "productname",
            "product_name",
            "item",
            "itemname",
            "item_name",
            "name",
            "title"
        ],

        "brand": [
            "brand",
            "company",
            "manufacturer",
            "make"
        ],

        "category": [
            "category",
            "subcategory",
            "sub_category",
            "group",
            "department",
            "type"
        ],

        "price": [
            "price",
            "saleprice",
            "sale_price",
            "sellingprice",
            "selling_price",
            "cost",
            "mrp",
            "marketprice",
            "market_price",
            "unitprice",
            "unit_price"
        ],

        "stock": [
            "stock",
            "quantity",
            "inventory",
            "availablequantity",
            "available_quantity"
        ],

        "rating": [
            "rating",
            "stars",
            "review",
            "reviewscore",
            "review_score"
        ],

        "supplier": [
            "supplier",
            "vendor",
            "distributor"
        ],

        "description": [
            "description",
            "details",
            "productdescription",
            "product_description"
        ]
    }

    def normalize(self, text: str) -> str:
        """
        Normalize a column name.
        Example:
        Sale Price -> saleprice
        sale_price -> saleprice
        SALE-PRICE -> saleprice
        """
        return re.sub(r'[^a-z0-9]', '', text.lower())

    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe.copy()

    def map_columns(self):

        normalized_columns = {
            self.normalize(col): col
            for col in self.df.columns
        }

        rename_dict = {}

        for standard_name, aliases in self.COLUMN_MAPPING.items():

            for alias in aliases:

                alias = self.normalize(alias)

                if alias in normalized_columns:

                    rename_dict[
                        normalized_columns[alias]
                    ] = standard_name

                    break

        self.df.rename(
            columns=rename_dict,
            inplace=True
        )

        return self.df