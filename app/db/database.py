from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from voron.app.models.base import Base
from voron.app.models import account
from voron.app.models import advertisiment

load_dotenv()

BD_USER = os.getenv("BD_USER")
BD_PASSWORD = os.getenv("BD_PASSWORD")
BD_HOST = os.getenv("BD_HOST")
BD_PORT = os.getenv("BD_PORT")
BD_NAME = os.getenv("BD_NAME")

print(BD_USER, BD_PASSWORD, BD_HOST, BD_PORT, BD_NAME)

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg://{BD_USER}:{BD_PASSWORD}@{BD_HOST}:{BD_PORT}/{BD_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit = False, autoflush=False, bind = engine)

Base.metadata.create_all(bind = engine)
    