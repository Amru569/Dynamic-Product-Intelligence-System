from app.loader import CSVLoader
from app.mapper import ColumnMapper
from app.validator import DataValidator

loader = CSVLoader("data/uploads/products.csv")

df = loader.load_csv()

mapper = ColumnMapper(df)

df = mapper.map_columns()

validator = DataValidator(df)

df = validator.validate()

print(df.head())

print(df.info())