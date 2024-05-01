from typing import List

from pydantic import BaseModel


class BaseSchema(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class ItemSchema(BaseSchema):
    category_id: int
    description: str
    image_url: str | None = None

    class Config:
        from_attributes = True


class ProductSchema(BaseModel):
    id: int
    item_id: int
    store_id: int
    price: float
    active: bool
    item: ItemSchema
    store: BaseSchema

    class Config:
        from_attributes = True
