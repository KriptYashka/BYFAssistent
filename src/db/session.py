import os.path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
import configparser
from threading import Lock


class SessionDB:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(SessionDB, cls).__new__(cls)
                    cls._instance._init_session()
        return cls._instance

    def _init_session(self):
        config = configparser.ConfigParser()
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'settings.ini'))
        config.read(path)
        db_url = config["DB"]["DATABASE_URL"]

        self._engine = create_engine(db_url, pool_pre_ping=True)
        self._SessionLocal = sessionmaker(bind=self._engine, autoflush=False, autocommit=False)

    def get_session(self) -> Session:
        """
        Возвращает новую сессию для работы с БД.
        Используйте контекстный менеджер для автоматического закрытия:

        with Session().get_session() as session:
            # работа с session
        """
        return self._SessionLocal()
