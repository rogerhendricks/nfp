import os
import databases
from sqlalchemy import Table, Column, Integer, String, Boolean, MetaData, create_engine
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

database = databases.Database(DATABASE_URL)

metadata = MetaData()

devices = Table(
    "devices",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("manufacturer", String),
    Column("model", String),
    Column("dev_type", String),
    Column("hazard", Boolean),
    Column("mri", Boolean),
)

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String),
    Column("hashed_password", String)
)


engine = create_engine(
    DATABASE_URL
)

metadata.create_all(engine)