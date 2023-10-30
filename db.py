from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from Appsetting import GetAppSetting

appsetting = GetAppSetting()
engine = create_engine(appsetting.serverEnv.prod, pool_timeout=1, pool_size=1, max_overflow=2) #,pool_recycle=True
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
def conDB():
    Session = SessionLocal()
    return Session
def closeDB(Session):
    Session.close()
    engine.dispose()


