import configparser

from sqlalchemy import create_engine
from repository.tables.base import Base

# Необходимо импортировать используемые модели
from repository.tables.dance_style import DanceStyle
from repository.tables.hall import Hall
from repository.tables.lesson import Lesson
from repository.tables.place import Place
from repository.tables.price import Price
from repository.tables.subscription_request import SubscriptionRequest
from repository.tables.teacher import Teacher
from repository.tables.timeslot import Timeslot
from repository.tables.user import User

def main():
    config = configparser.ConfigParser()
    config.read("settings.ini")
    db_url = config["DB"]["DATABASE_URL"]

    engine = create_engine(db_url)
    Base.metadata.create_all(engine)

    print("Таблицы успешно созданы!")

if __name__ == '__main__':
    main()
