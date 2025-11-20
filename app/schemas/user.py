from pydantic import BaseModel, EmailStr, Field

data = {
    "id": 1,
    "username": "anonymous",
    "email": "anonymous@example.com",
    "password": "securepassword",
}

class UserCreate(BaseModel):
    id: int
    username: str = Field(default="anonymous", min_length=5, max_length=50)
    email: EmailStr
    password: str = Field(min_length=8)

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str