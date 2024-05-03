from typing import List

from pydantic import BaseModel, validator


class BaseSchema(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class ItemSchema(BaseSchema):
    category_id: int
    description: str
    image_url: str | None = None

    @validator('image_url', pre=True, always=True)
    def set_image_url(cls, v):
        return f"http://127.0.0.1:8000/static/{v}"

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
