from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ...config.application import settings

engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URI,
    echo=True,
    # Проверяет, живо ли соединение, и повторно подключается, если нет.
    # Имеет небольшие накладные расходы (отправляет SELECT 1 ).
    pool_pre_ping=True,
    # connect_args={'check_same_thread': False},
)

# Unless you use autocommit=True, the transaction is started automatically,
# and therefore you do not need to call session.begin() explicitly.
Session = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)

def get_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()