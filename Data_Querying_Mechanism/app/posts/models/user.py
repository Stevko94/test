from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..db.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    posts = relationship("Post", back_populates="user")
    comments = relationship("Comment", back_populates="user")
