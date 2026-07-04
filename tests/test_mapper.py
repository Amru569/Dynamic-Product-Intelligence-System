from app.loader import CSVLoader
from app.mapper import ColumnMapper

loader = CSVLoader("data/uploads/products.csv")

df = loader.load_csv()

print("Original Columns")
print(df.columns.tolist())

mapper = ColumnMapper(df)

df = mapper.map_columns()

print("\nMapped Columns")
print(df.columns.tolist())