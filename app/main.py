from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from .register import api_router
import sys
from alembic.config import Config
from alembic import command
import os

from app.core.db.default_data.import_bulk_default_data import import_bulk_default_data

app = FastAPI(
    title='SABSEG-FastAPI',
    openapi_url=f"{'/api/v1'}/openapi.json"
)

alembic_config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'alembic.ini')
print("alembic_config_path",alembic_config_path)
@app.on_event("startup")
async def startup_event():
    # alembic_cfg = Config(alembic_config_path)
    # command.upgrade(alembic_cfg, 'head')
    
    import_bulk_default_data()
    print("Project started")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix='/api/v1')

