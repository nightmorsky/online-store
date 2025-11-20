import os
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import uvicorn
from pydantic import BaseModel
from app.schemas.user import UserCreate, UserLogin, Token
from fastapi.responses import HTMLResponse

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
DB_URL = os.getenv("DB_URL")

app = FastAPI()


@app.post("/user/")
async def create_user(user: UserCreate):
    return {"success": True, "message": "User created successfully", "user": user}

@app.get("/home/")
async def read_root():
    return HTMLResponse(content="<h1>Welcome to the Online Store API</h1>", status_code=200)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
