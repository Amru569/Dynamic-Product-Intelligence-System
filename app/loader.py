import os
import pandas as pd


class CSVLoader:
    """
    Handles loading CSV files safely.
    """

    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_csv(self) -> pd.DataFrame:
        """
        Loads a CSV file into a Pandas DataFrame.

        Returns:
            pd.DataFrame

        Raises:
            FileNotFoundError
            ValueError
        """

        # Check if file exists
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(
                f"CSV file not found: {self.file_path}"
            )

        # Check extension
        if not self.file_path.lower().endswith(".csv"):
            raise ValueError(
                "Uploaded file is not a CSV file."
            )

        # Try reading using UTF-8
        try:
            df = pd.read_csv(self.file_path)

        # Fallback encoding
        except UnicodeDecodeError:
            df = pd.read_csv(
                self.file_path,
                encoding="latin1"
            )

        # Empty file check
        if df.empty:
            raise ValueError(
                "CSV file is empty."
            )

        return df