import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Carregar variáveis de ambiente
load_dotenv()
postgres_user = os.getenv("postgres_user")
root_pw = os.getenv("root_pw")
postgres_db = os.getenv("postgres_db")

# Configuração do banco de dados
DATABASE_URL = f"postgresql://{postgres_user}:{root_pw}@localhost/{postgres_db}"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Data(Base):
    __tablename__ = 'data'
    timestamp = Column(DateTime, primary_key=True)
    wind_speed = Column(Float)
    power = Column(Float)
    ambient_temperature = Column(Float)

# Criação da tabela no banco de dados
Base.metadata.create_all(engine)
