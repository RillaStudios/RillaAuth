from fastapi import APIRouter

app_router = APIRouter()

@app_router.get("/system_check")
def check():
    return {"status": "ok"}
