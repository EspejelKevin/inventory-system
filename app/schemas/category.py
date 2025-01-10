from pydantic import BaseModel


class CategoryInput(BaseModel):
    name: str
    description: str


class CategoryOutput(BaseModel):
    id: int
    name: str
    description: str
