import uvicorn
from fastapi import FastAPI
from db.base import database
from core.config import APP_ADDR, APP_PORT
from endpoints import users

app = FastAPI(title="Employment exchange")
app.include_router(users.router, prefix="/users", tags=["users"])

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


if __name__ == '__main__':
    uvicorn.run("main:app", port=APP_PORT, host=APP_ADDR, reload=True)