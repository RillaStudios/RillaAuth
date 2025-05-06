from contextlib import asynccontextmanager

from app.db.bootstrap_db.bootstrap_db import BootstrapDb


@asynccontextmanager
async def lifespan(auth_app):
    print("Starting setup mode...")
    BootstrapDb.init_db()
    yield
    print("Shutting down...")