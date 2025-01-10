from pydantic import BaseModel


class ProductInput(BaseModel):
    name: str
    description: str
    cost: float
    price: float
    stock: int
    sku: str
    category_id: int


class ProductOutput(BaseModel):
    id: int
    name: str
    description: str
    cost: float
    price: float
    stock: int
    sku: str
    category: str
