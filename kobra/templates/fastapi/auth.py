from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from passlib.context import CryptContext
from config import Config

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/token")
async def login(data: dict):
    username = data.get("username")
    password = data.get("password")
    # Implemente lógica de autenticação aqui
    token = jwt.encode({"sub": username}, Config.SECRET_KEY, algorithm="HS256")
    return {"access_token": token, "token_type": "bearer"}