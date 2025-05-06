import sys
from fastapi import APIRouter

from app.db.bootstrap_db.bootstrap_db import BootstrapDb
from app.system.system_check import SystemHealthCheck
import sqlite3

service_router = APIRouter()

@service_router.get("/system-check")
def check() -> SystemHealthCheck:

    health_check = SystemHealthCheck()

    # Check if SQLite database has information
    try:
        # Connect to the database - adjust the path to your actual database location
        conn = sqlite3.connect("your_database.db")
        cursor = conn.cursor()

        # Query to check if database has tables with data
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()

        if not tables:
            health_check.db_running = False
        else:
            # Additional check could verify if specific tables have data
            health_check.db_running = True

        conn.close()
    except Exception as e:
        # If any error occurs during database check, set db_running to False
        check.db_running = False
        print(f"Database check error: {e}", file=sys.stderr)

    # Return the SystemCheck object, not a dictionary
    return health_check
