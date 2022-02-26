from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy import Column,Integer,String
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship,backref

@dataclass
class AddressModel(db.Model):
    cep:str
    city:str
    district: str
    street:str
    House_number:int
    complement:str

    __tablename__ = 'address'

    cep = Column(String,nullable=False)
    city = Column(String,nullable=False)
    district = Column(String,nullable=False)
    street = Column(String,nullable=False)
    House_number = Column(Integer,nullable=False)
    complement = Column(String,default="none")

    user_id = Column(Integer,ForeignKey('user.id'), nullable=False,unique=True)

    user = relationship("UserModel",backref=backref("address",uselist=False))