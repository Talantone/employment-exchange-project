from starlette.config import Config

config = Config(".env_dev")

DATABASE_URL = config("DATABASE_URL", cast=str, default="")
APP_ADDR = config("APP_ADDR", cast=str, default="127.0.0.1")
APP_PORT = config("APP_PORT", cast=int, default=8000)