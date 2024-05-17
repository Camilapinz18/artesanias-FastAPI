# fastapi
from fastapi import Depends, UploadFile, File
from fastapi import HTTPException
from fastapi import Request

# route
from ..register import rooms_router

# session
from app.core.db.session import get_db
from sqlalchemy.orm import Session

# provider
from app.modules.products.providers.products import Product as ProductProvider

# schemas
from app.modules.rooms.schemas.room import RoomPost, RoomUpdate
from app.modules.rooms.schemas.available_rooms import AvailableRoomPost

@rooms_router.get("")
def get_all_products(
    db_session: Session = Depends(get_db)
):
    return ProductProvider.get_all_products(db_session)


