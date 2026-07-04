from app.loader import CSVLoader

loader = CSVLoader(
    "data/uploads/BigBasket Products.csv"
)

df = loader.load_csv()

print(df.head())

print(df.columns.tolist())