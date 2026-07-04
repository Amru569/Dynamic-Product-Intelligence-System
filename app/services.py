from sqlalchemy.orm import Session

from app.models import Product
from app.loader import CSVLoader
from app.mapper import ColumnMapper
from app.validator import DataValidator

from app.index_manager import product_index


class ProductService:
    """
    Handles all business logic for the platform.
    """

    @staticmethod
    def upload_csv(file_path: str, db: Session):

        # ==========================================
        # Load CSV
        # ==========================================

        loader = CSVLoader(file_path)

        df = loader.load_csv()

        total_records = len(df)

        # ==========================================
        # Dynamic Column Mapping
        # ==========================================

        mapper = ColumnMapper(df)

        df = mapper.map_columns()

        print("\n" + "=" * 60)
        print("Mapped Columns")
        print(df.columns.tolist())
        print("=" * 60)

        # ==========================================
        # Validate Dataset
        # ==========================================

        validator = DataValidator(df)

        df = validator.validate()

        cleaned_records = len(df)

        # ==========================================
        # Remove Previous Records
        # ==========================================

        db.query(Product).delete()

        db.commit()

        # ==========================================
        # Convert DataFrame -> ORM Objects
        # ==========================================

        products = []

        for _, row in df.iterrows():

            product = Product(

                product_name=row["product_name"],

                brand=row["brand"],

                category=row["category"],

                supplier=row["supplier"],

                description=row["description"],

                price=float(row["price"]),

                stock=int(row["stock"]),

                rating=float(row["rating"])

            )

            products.append(product)

        # ==========================================
        # Bulk Insert
        # ==========================================

        db.bulk_save_objects(products)

        db.commit()

        # ==========================================
        # Build Product Index
        # ==========================================

        all_products = db.query(Product).all()

        product_index.build(all_products)

        print()

        print("=" * 60)
        print(f"Indexed {product_index.total_products} products")
        print("=" * 60)

        # ==========================================
        # Return Response
        # ==========================================

        return {

            "status": "success",

            "message": "Dataset uploaded successfully.",

            "total_records": total_records,

            "cleaned_records": cleaned_records,

            "inserted_records": len(products),

            "skipped_records": total_records - cleaned_records

        }

    @staticmethod
    def get_all_products(db: Session):

        return db.query(Product).all()

    @staticmethod
    def get_product_by_id(product_id: int, db: Session):

        return (

            db.query(Product)

            .filter(Product.id == product_id)

            .first()

        )

    @staticmethod
    def delete_all_products(db: Session):

        deleted = db.query(Product).delete()

        db.commit()

        return {

            "status": "success",

            "deleted_records": deleted

        }