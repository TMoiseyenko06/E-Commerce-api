from database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey

class Role(Base):
    __tablename__ = 'roles'
    id: Mapped[int] = mapped_column(primary_key=True)
    role_name: Mapped[str] = mapped_column(String(32), unique=True, nullable=False)

class UserManagment(Base):
    __tablename__ = 'user_managment'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    role_id: Mapped[int] = mapped_column(ForeignKey('roles.id'))