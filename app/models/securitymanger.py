import os
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.database import Base
from dotenv import load_dotenv

class SecurityManager(Base):
    __tablename__ = "security_managers"
    manager_id = Column(Integer, primary_key=True, index=True)
    organization_id = Column(Integer, ForeignKey("organizations.organization_id"))
    password = Column(String, nullable=False)
    name = Column(String)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String)

    organization = relationship("Organization", back_populates="managers")