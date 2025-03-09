from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from app.configs import DB_URI


engine = create_engine(DB_URI)
Session = scoped_session(sessionmaker(bind=engine))
