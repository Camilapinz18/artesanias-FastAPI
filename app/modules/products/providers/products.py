from fastapi import HTTPException
from sqlalchemy.orm import aliased

from sqlalchemy import func, distinct
from sqlalchemy.sql import and_, or_, not_ # Import the necessary logical operators
from sqlalchemy.sql.expression import literal_column

# models:
from app.modules.products.models.product import Product as ProductModel


class Product():

    def get_all_products(db_session):
        try:

            return db_session.query(ProductModel).all()
        
        except Exception as e:
            raise HTTPException(
                detail = "Ha ocurrido un error interno",
                status_code = 500
            )