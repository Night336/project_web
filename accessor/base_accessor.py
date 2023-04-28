from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class BaseAccessor:
    def __init__(self, path_db):
        self.engine = create_engine(path_db, echo=True)
        session = sessionmaker(bind=self.engine)
        self.session = session()

