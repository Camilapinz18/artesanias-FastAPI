from fastapi import HTTPException
from sqlalchemy.orm import aliased

from sqlalchemy import func, distinct
from sqlalchemy.sql import and_, or_, not_ # Import the necessary logical operators
from sqlalchemy.sql.expression import literal_column

# models:
from app.modules.rooms.models.room import Room as RoomModel
from ..models.room_category import RoomCategory
from app.modules.reservations.models.reservation import Reservation as ReservationModel


class Product():
    def create_room(room, db_session):
        created = RoomModel(**room.dict())
        db_session.add(created)
        
        db_session.commit()
        
        return {"msg": f"Se han creado la sala exitosamente"}

    def get_rooms(db_session):
        try:
            return db_session.query()
        except Exception as e:
            raise HTTPException(
                detail = "Ha ocurrido un error interno",
                status_code = 500
            )