from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    create_engine,
    DateTime,
    Boolean,
)
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker, declarative_base

# DB管理
DATABASE = "postgresql"
USER = "book_user"
PASSWORD = "souta0925"
HOST = "localhost"
PORT = "5432"
DB_NAME = "book_date"

URL = f"{DATABASE}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
engine = create_engine(URL, echo=True)

Base = declarative_base()
Connection = sessionmaker(bind=engine)
connection = Connection()


class Books(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    volume = Column(String(255))
    author = Column(String(255))
    publisher = Column(String(255))
    memo = Column(Text)
    create_date = Column(DateTime(timezone=True), default=func.now(), nullable=False)
    delFlg = Column(Boolean)


class BookUser(Base):
    __tablename__ = "book_user"
    user_id = Column(String(255), primary_key=True)
    passwd = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    user_shi = Column(String(255))
    user_mei = Column(String(255))
    delFlg = Column(Boolean)


if __name__ == "__main__":
    Base.metadata.create_all(engine)
