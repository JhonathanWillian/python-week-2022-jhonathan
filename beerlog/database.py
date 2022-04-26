import beerlog
from sqlmodel import create_engine
from beerlog.config import settings

engine = create_engine(settings.database.url)

models.SQLModel.metadata.create_all(engine)