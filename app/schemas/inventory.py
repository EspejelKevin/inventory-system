from datetime import date

from pydantic import BaseModel


class InventoryInput(BaseModel):
    quantity: int
    update_date: date
    description: str
    movement_type: str
    product_id: int
    code: str


class InventoryOutput(BaseModel):
    id: int
    quantity: int
    update_date: date
    description: str
    movement_type: str
    product: str
    code: str
