from starlette.config import Config

config = Config(".env_dev")

DATABASE_URL = config("DATABASE_URL", cast=str, default="")
ACCESS_EXPIRATION = config("ACCESS_EXP",  cast=int, default=60) #expiration in minutes
APP_ADDR = config("APP_ADDR", cast=str, default="127.0.0.1")
APP_PORT = config("APP_PORT", cast=int, default=8000)
ALGORITHM = "HS256"
SECRET_KEY = config("SECRET_KEY", cast=str, default="e85c176dcd430bd9306b995afba0a47f399669cf4762c9d609d92b5f55da7626")