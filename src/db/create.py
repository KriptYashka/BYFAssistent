import configparser

from sqlalchemy import create_engine
from repository.tables.base import Base

# Необходимо импортировать используемые модели
from src.db.repository.tables.dance_style import DanceStyle
from src.db.repository.tables.hall import Hall
from src.db.repository.tables.lesson import Lesson
from src.db.repository.tables.place import Place
from src.db.repository.tables.price import Price
from src.db.repository.tables.subscription_request import SubscriptionRequest
from src.db.repository.tables.teacher import Teacher
from src.db.repository.tables.timeslot import Timeslot
from src.db.repository.tables.user import User

def main():
    config = configparser.ConfigParser()
    config.read("settings.ini")
    db_url = config["DB"]["DATABASE_URL"]

    engine = create_engine(db_url)
    Base.metadata.create_all(engine)

    print("Таблицы успешно созданы!")

if __name__ == '__main__':
    main()
