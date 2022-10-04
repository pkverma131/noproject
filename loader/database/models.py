from sqlalchemy import Integer, String, Column, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Brand(Base):
    __tablename__ = 'core_brand'
    id = Column(Integer, primary_key=True)
    input_type = Column(String(50), nullable=False)
    output_type = Column(String(50), nullable=False)
    output_file = Column(String(200),  nullable=False)
    status =  Column(Boolean, default=False)
    #created_on = Column(DateTime, default=datetime.now)
    #updated_on = Column(DateTime, default=datetime.now, onupdate=datetime.now)
