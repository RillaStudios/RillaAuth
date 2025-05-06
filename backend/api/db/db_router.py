import sqlite3

from fastapi import APIRouter

db_router = APIRouter()

# @db_router.get("/initialized")
# def setup_needed():
#     try:
#         settings = load_db_settings()
#         return {"is_setup": settings is not None}
#     except sqlite3.OperationalError as e:
#         if "no such table" in str(e):
#             print("no such table")
#             return {"is_setup": False}
#         raise