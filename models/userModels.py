from database import db, Base
from sqlalchemy.orm import Mapped,mapped_column
from typing import List
from werkzeug.security import check_password_hash
from models.roleModels import Role

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(db.Integer,primary_key=True)
    name: Mapped[str] = mapped_column(db.String(255),nullable=False)
    username: Mapped[str] = mapped_column(db.String(255),nullable=False)
    hashed_pass: Mapped[str] = mapped_column(db.String(500),nullable=False)
    roles: Mapped[List[Role]] = db.relationship(secondary="user_managment") 

    def check_password(self,password):
        return check_password_hash(self.hashed_pass,password)


