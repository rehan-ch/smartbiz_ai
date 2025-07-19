from pydantic import BaseModel
from typing import Optional
from app.schemas.category import CategoryOut

class ProductBase(BaseModel):
    name: str
    sku: str
    price: float
    stock: int

class ProductCreate(ProductBase):
    category_id: Optional[int]  # 👈 allow assigning category

class ProductOut(ProductBase):
    id: int
    category: Optional[CategoryOut]  # 👈 include nested category

    class Config:
        orm_mode = True
