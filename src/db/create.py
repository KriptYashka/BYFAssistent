from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tables.user import Base as

DATABASE_URL = "postgresql+psycopg2://root:root@localhost:5432/db_byf"

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

print("Таблица users успешно создана!")
