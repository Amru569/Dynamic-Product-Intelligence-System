import pandas as pd


class DataValidator:
    """
    Validate and clean a Product/Inventory DataFrame.
    """

    REQUIRED_COLUMNS = ["product_name", "price"]

    OPTIONAL_COLUMNS = {
        "brand": "Unknown",
        "category": "Unknown",
        "supplier": "Unknown",
        "description": "",
        "stock": 0,
        "rating": 0.0,
    }

    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe.copy()

    def validate(self) -> pd.DataFrame:

        # -----------------------------------
        # Standardize column names
        # -----------------------------------

        self.df.columns = (
            self.df.columns
            .str.strip()
            .str.lower()
        )

        # -----------------------------------
        # Check required columns
        # -----------------------------------

        missing = [
            col
            for col in self.REQUIRED_COLUMNS
            if col not in self.df.columns
        ]

        if missing:
            raise ValueError(
                f"Missing required columns: {missing}"
            )

        # -----------------------------------
        # Remove duplicate rows
        # -----------------------------------

        self.df.drop_duplicates(inplace=True)

        # -----------------------------------
        # Clean string columns
        # -----------------------------------

        object_columns = self.df.select_dtypes(
            include="object"
        ).columns

        for col in object_columns:

            self.df[col] = (
                self.df[col]
                .fillna("")
                .astype(str)
                .str.strip()
            )

        # -----------------------------------
        # Convert numeric columns
        # -----------------------------------

        self.df["price"] = pd.to_numeric(
            self.df["price"],
            errors="coerce"
        )

        if "stock" in self.df.columns:

            self.df["stock"] = pd.to_numeric(
                self.df["stock"],
                errors="coerce"
            )

        if "rating" in self.df.columns:

            self.df["rating"] = pd.to_numeric(
                self.df["rating"],
                errors="coerce"
            )

        # -----------------------------------
        # Remove invalid products
        # -----------------------------------

        self.df = self.df[
            self.df["product_name"] != ""
        ]

        self.df = self.df[
            self.df["price"].notna()
        ]

        self.df = self.df[
            self.df["price"] >= 0
        ]

        # -----------------------------------
        # Fill optional columns
        # -----------------------------------

        for column, default in self.OPTIONAL_COLUMNS.items():

            if column not in self.df.columns:

                self.df[column] = default

            else:

                self.df[column] = self.df[column].fillna(default)

        # -----------------------------------
        # Keep only required columns
        # -----------------------------------

        self.df = self.df[

            [

                "product_name",

                "brand",

                "category",

                "supplier",

                "description",

                "price",

                "stock",

                "rating"

            ]

        ]

        return self.df.reset_index(drop=True)