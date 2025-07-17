from typing import Optional
from pydantic import BaseModel

# Shared properties
class ProductBase(BaseModel):
    name: str
    sku: str
    price: float
    stock: int = 0

# For creating new product
class ProductCreate(ProductBase):
    pass

# For updating product (all fields optional)
class ProductUpdate(BaseModel):
    name: Optional[str]	 = None
    sku: Optional[str] = None
    price: Optional[float]	 = None
    stock: Optional[int]	 = None

# For response
class ProductOut(ProductBase):
    id: int

    class Config:
        orm_mode = True
