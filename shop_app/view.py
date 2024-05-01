from typing import List

from sqlalchemy.orm import Session

from . import models, schemas


def get_products(db: Session, skip: int = 0, limit: int = 20, search: str = "", cat: List[int] = None,
                 store: List[int] = None):
    search_term = f"%{search}%"
    query = db.query(models.Product).join(models.Item)

    if search:
        query = query.filter(models.Item.name.ilike(search_term))

    if cat:
        query = query.filter(models.Item.category_id.in_(cat))

    if store:
        query = query.filter(models.Product.store_id.in_(store))

    return query.offset(skip).limit(limit).all()
