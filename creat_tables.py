from accessor import Accessor
from data import Base

if __name__ == "__main__":
    a = "sqlite:///db//my_database.db"
    accessor = Accessor(a)
    Base.metadate.create_all(accessor.engine)
