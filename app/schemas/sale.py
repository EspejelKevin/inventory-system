from datetime import date

from pydantic import BaseModel


class SaleDetails(BaseModel):
    quantity: int
    price: float
    total_price: float
    product_id: int


class SaleInput(BaseModel):
    client_id: int
    seller_id: int
    details: SaleDetails | list[SaleDetails]


class Sale(BaseModel):
    folio: str
    subtotal: float
    total: float
    sale_date: date = date.today()


class SaleOutput(BaseModel):
    id: int
    folio: str
    client: str
    seller: str
    sale_date: date
    subtotal: float
    total: float
    details: SaleDetails | list[SaleDetails]
