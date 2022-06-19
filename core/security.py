import datetime

from passlib.context import CryptContext
from jose import jwt

from .config import ACCESS_EXPIRATION, SECRET_KEY, ALGORITHM

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(password: str, hash: str) -> bool:
    return pwd_context.verify(password, hash)

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    to_encode.update({"exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=ACCESS_EXPIRATION)})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_access_token(token: str):
    try:
        encoded_jwt = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
    except jwt.JWSError:
        return None
    return encoded_jwt
