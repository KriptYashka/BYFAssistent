import configparser

from sqlalchemy import create_engine
from src.db.repository.base import Base

# Необходимо импортировать используемые модели
from src.db.repository.dance_style import DanceStyle
from src.db.repository.hall import Hall
from src.db.repository.lesson import Lesson
from src.db.repository.place import Place
from src.db.repository.teacher import Teacher
from src.db.repository.timeslot import Timeslot
from src.db.repository.user import User

def main():
    config = configparser.ConfigParser()
    config.read("settings.ini")
    db_url = config["DB"]["DATABASE_URL"]

    engine = create_engine(db_url)
    Base.metadata.create_all(engine)

    print("Таблицы успешно созданы!")

if __name__ == '__main__':
    main()
