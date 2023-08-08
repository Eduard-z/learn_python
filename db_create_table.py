import os
from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.orm import declarative_base, sessionmaker


if os.path.exists("some.db"):
    os.remove("some.db")
engine = create_engine("sqlite:///some.db", echo=True)  # Соединение с базой данных

Base = declarative_base()  # новый класс, который мы назвали Base, от которого будет унаследованы все наши ORM-классы
Session = sessionmaker()  # служит фабрикой объектов сессий


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String, nullable=False)
    password = Column(String)

    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.name, self.fullname, self.password)


# Создание таблицы
Base.metadata.create_all(engine)

print(User.__table__)  # объект Table, что создан нашей версией User, доступен через атрибут __table__
print(Base.metadata)  # метаданные MetaData также доступны

Session.configure(bind=engine)  # соедините подключение к базе с сессией

# Добавление новых объектов
session = Session()
vasiaUser = User("vasia", "Vasiliy Pypkin", "vasia2000")
session.add(vasiaUser)

ourUser = session.query(User).filter_by(name="vasia").first()
print(ourUser)  # <User('vasia','Vasiliy Pypkin', 'vasia2000')>

# сменим пароль
vasiaUser.password = "-=VP2001=-"
# добавить сразу пачку записей
session.add_all([User("kolia", "Cool Kolian[S.A.]", "kolia$$$"), User("zina", "Zina Korzina", "zk18")])

print(vasiaUser.id)
print(vasiaUser.password)

session.commit()  # сбрасывает все оставшиеся изменения в базу и фиксирует транзакции
print(vasiaUser.id)
print(vasiaUser.password)

vasiaUser.name = 'Vaska'
print(vasiaUser.name)

# добавим ошибочного пользователя
fake_user = User('fakeuser', 'Invalid', '12345')
session.add(fake_user)

with engine.connect() as conn:
    conn.execute(
        text("INSERT INTO users (name, fullname, password) VALUES (:x, :y, :z)"),
        [{"x": 1, "y": 1, "z": None}, {"x": 2, "y": 4, "z": 4}],
    )
    conn.commit()
