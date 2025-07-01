import os
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.database import Base
from dotenv import load_dotenv

#조직 테이블 
class Organization(Base):
    __tablename__ = "organizations"
    organization_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    managers = relationship("SecurityManager", back_populates="organization")

