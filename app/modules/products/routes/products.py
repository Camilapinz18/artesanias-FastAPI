# fastapi
from fastapi import Depends, UploadFile, File
from fastapi import HTTPException
from fastapi import Request

# route
from ..register import products_router

# session
from app.core.db.session import get_db
from sqlalchemy.orm import Session

# provider
from app.modules.products.providers.products import Product as ProductProvider

# schemas

@products_router.get("")
def get_all_products(
    db_session: Session = Depends(get_db)
):
    return ProductProvider.get_all_products(
        db_session
    )


