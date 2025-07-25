## se hace la coneccion a la base de datos usando mysql
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# URL de conexión 
database_url = "mysql+pymysql://root:@localhost:3306/flutterdb"

# Crear el engine
engine = create_engine(database_url)

# Crear una sesión local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base declarativa
base = declarative_base()


def get_db():
    """Dependencia para obtener la sesión de base de datos"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
