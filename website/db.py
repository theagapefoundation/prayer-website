import os
from sqlmodel import create_engine

engine = create_engine(os.environ.get("DATABASE_URL"))
