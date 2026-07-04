from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime


class ProductBase(BaseModel):
    """
    Common Product Fields
    """

    product_name: str = Field(..., min_length=1, max_length=255)
    brand: Optional[str] = None
    category: Optional[str] = None
    supplier: Optional[str] = None
    description: Optional[str] = None
    price: float = Field(..., ge=0)
    stock: Optional[int] = Field(default=None, ge=0)
    rating: Optional[float] = Field(default=None, ge=0, le=5)


class ProductCreate(ProductBase):
    """
    Schema used while inserting products.
    """
    pass


class ProductResponse(ProductBase):
    """
    Schema returned by the API.
    """

    id: int
    uploaded_at: datetime

    model_config = ConfigDict(from_attributes=True)


class UploadResponse(BaseModel):
    """
    Response after CSV upload.
    """

    status: str
    message: str
    total_records: int
    inserted_records: int
    skipped_records: int