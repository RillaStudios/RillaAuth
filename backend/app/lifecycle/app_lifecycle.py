from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(auth_app):
    print("Starting setup mode...")
    yield
    print("Shutting down...")