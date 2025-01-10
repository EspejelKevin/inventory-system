from pydantic import BaseModel


class ProductInput(BaseModel):
    name: str
    description: str
    cost: float
    price: float
    stock: int
    category_id: int


class Product(ProductInput):
    sku: str


class ProductOutput(BaseModel):
    id: int
    name: str
    description: str
    cost: float
    price: float
    stock: int
    sku: str
    category: str
