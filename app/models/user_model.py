from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy import Column,Integer,String
from app.exceptions import WrongKeysError,InvalidValueError
from werkzeug.security import generate_password_hash,check_password_hash

@dataclass
class UserModel(db.Model):
    id:int
    name:str
    email:str
    cep:str
    city:str
    district: str
    street:str
    House_number:int
    complement:str

    __tablename__ = 'user'

    id = Column(Integer,primary_key=True)
    name = Column(String,nullable=False)
    email = Column(String,nullable=False,unique=True)
    cep = Column(String,nullable=False)
    password_hash = Column(String,nullable=False)
    city = Column(String,nullable=False)
    district = Column(String,nullable=False)
    street = Column(String,nullable=False)
    House_number = Column(Integer,nullable=False)
    complement = Column(String,default="none")

    @property
    def password(self):
        raise AttributeError('password is not acessible')

    @password.setter
    def password(self,password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)


    def check_password(self,password_to_compare):
        return check_password_hash(self.password_hash,password_to_compare)


    @staticmethod
    def check_data(data:dict):
        expected_data = {
            "name":str,
            "email":str,
            "password":str,
            "cep":str,
            "city":str,
            "district":str,
            "street":str,
            "House_number":int
        }
        validated_data = {}
        for key,value_type in expected_data.items():
            item_received = data.get(key)

            if (not item_received):
                raise WrongKeysError(data,expected_data)

            elif (value_type != type(item_received)):
                raise InvalidValueError(data,expected_data)

            else:
                validated_data[key] = item_received
        
        complement = data.get("complement")
        if(complement):
            validated_data["complement"] = complement
        
        return validated_data