import os
import shutil

from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import Depends
from fastapi import Query

from sqlalchemy.orm import Session

from app.database import get_db
from app.services import ProductService
from app.search import SearchEngine
from app.lookup import ProductLookup
from app.compare import PriceComparisonEngine

router = APIRouter()

UPLOAD_FOLDER = "data/uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ==========================================================
# Upload Dataset
# ==========================================================

@router.post("/upload")
def upload_dataset(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    if not file.filename.lower().endswith(".csv"):

        return {
            "status": "error",
            "message": "Only CSV files are allowed."
        }

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(file_path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    return ProductService.upload_csv(
        file_path=file_path,
        db=db
    )


# ==========================================================
# Trie Search
# ==========================================================

@router.get("/search")
def search_products(

    q: str = Query(...)

):

    engine = SearchEngine()

    results = engine.search(q)

    return {

        "keyword": q,

        "count": len(results),

        "results": results

    }


# ==========================================================
# Product Lookup
# ==========================================================

@router.get("/product")
def get_product(

    name: str

):

    lookup = ProductLookup()

    product = lookup.get_product(name)

    if product is None:

        return {

            "status": "error",

            "message": "Product not found."

        }

    return {

        "id": product.id,

        "product_name": product.product_name,

        "brand": product.brand,

        "category": product.category,

        "supplier": product.supplier,

        "description": product.description,

        "price": product.price,

        "stock": product.stock,

        "rating": product.rating

    }


# ==========================================================
# Cheapest Product
# ==========================================================

@router.get("/cheapest")
def cheapest_product():

    engine = PriceComparisonEngine()

    product = engine.cheapest_product()

    if product is None:

        return {

            "status": "error",

            "message": "No products available."

        }

    return {

        "price": product[0],

        "product_id": product[1],

        "product_name": product[2]

    }


# ==========================================================
# Top Cheapest Products
# ==========================================================

@router.get("/top-cheapest")
def top_cheapest(

    limit: int = 10

):

    engine = PriceComparisonEngine()

    products = engine.top_cheapest(limit)

    result = []

    for price, pid, name in products:

        result.append({

            "product_id": pid,

            "product_name": name,

            "price": price

        })

    return {

        "count": len(result),

        "products": result

    }


# ==========================================================
# All Products
# ==========================================================

@router.get("/products")
def get_products(

    db: Session = Depends(get_db)

):

    products = ProductService.get_all_products(db)

    return {

        "total": len(products),

        "products": products

    }


# ==========================================================
# Delete Products
# ==========================================================

@router.delete("/products")
def delete_products(

    db: Session = Depends(get_db)

):

    return ProductService.delete_all_products(db)