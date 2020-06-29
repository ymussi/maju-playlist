from sqlalchemy import Column, Integer, String, JSON, DateTime, Float
from sqlalchemy.sql import func
from maju.database import Base, Model


class LogCityTemp(Model):
    
    __tablename__ = 'log_city_temp'
    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    city = Column(String(244))
    uf = Column(String(244))
    temp = Column(String(244))
    music_gender = Column(String(244))
    provider = Column(String(244))
    status = Column(String(244))
    created = Column(DateTime(timezone=True), default=datetime.now())
    weather_response = Column(JSON())
    provider_response = Column(JSON())
