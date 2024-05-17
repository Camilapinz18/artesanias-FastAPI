from app.core.db.session import SessionLocal


from app.core.db.default_data.scripts.roles.roles import import_roles
from app.core.db.default_data.scripts.users.users import import_users


def import_bulk_default_data():
    print("Importing bulk default data")
    try:
        db_session = SessionLocal()

        import_roles(db_session)
        import_users(db_session)

        db_session.commit()
    except Exception as e:
        raise e
    finally:
        db_session.close()