from pydantic import BaseModel


class ClientInput(BaseModel):
    name: str
    lastname: str
    phone: str
    address: str
    email: str


class ClientOutput(BaseModel):
    id: int
    name: str
    lastname: str
    phone: str
    address: str
    email: str
