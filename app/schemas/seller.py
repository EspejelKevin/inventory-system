from pydantic import BaseModel


class SellerInput(BaseModel):
    name: str
    lastname: str
    phone: str
    address: str
    company: str


class SellerOutput(BaseModel):
    id: int
    name: str
    lastname: str
    phone: str
    address: str
    company: str
