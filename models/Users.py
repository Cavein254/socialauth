import uuid
from sqlalchemy import (
    LargeBinary,
    Column,
    String,
    Integer,
    Boolean,
    UniqueConstraint,
    PrimaryKeyConstraint,
)
from sqlalchemy_utils import UUIDType
from db import Base


class User(Base):
    """Creates a user table"""

    __tablename__ = "users"
    user_id = Column(
        UUIDType(binary=False),
        primary_key=True,
        default=uuid.uuid4,
        name=Column(String),
    )
    phone = Column(String(20), nullable=True, unique=True)
    email = Column(String(256), nullable=False, unique=True)
    hashed_password = Column(LargeBinary, nullable=False)
    fullname = Column(String(150), nullable=True)
    username = Column(String(50), nullable=True)
    is_active = Column(Boolean, default=False)

    UniqueConstraint("email", name="user_unique_email")
    PrimaryKeyConstraint("user_id", name="user_pk")

    def __repr__(self):
        """Representation of the model instance"""
        return "<User {email}>".format(email=self.email)
