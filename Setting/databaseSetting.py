from Appsetting import GetAppSetting
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


appsetting = GetAppSetting()
engine = create_engine(appsetting.serverEnv.prod, pool_timeout=28000, pool_size=10, max_overflow=20)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()