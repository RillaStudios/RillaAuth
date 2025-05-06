from contextlib import asynccontextmanager

from app.db.bootstrap_db.bootstrap_db import BootstrapDb
from app.lifecycle.startup import Startup


@asynccontextmanager
async def lifespan(auth_app):
    Startup().run()
    yield
    print("Shutting down...")