import configparser

from sqlalchemy import create_engine
from repository.tables.base import Base

# Необходимо импортировать используемые модели
import repository

def main():
    config = configparser.ConfigParser()
    config.read("settings.ini")
    db_url = config["DB"]["DATABASE_URL"]

    engine = create_engine(db_url)
    Base.metadata.create_all(engine)

    print("Таблицы успешно созданы!")

if __name__ == '__main__':
    main()
