"""
Implementation notes:
    1) I choose to use unittest library for testing.
    2) In-memory db as I know better for testing. Faster...
"""
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel

from sqlalchemy import Column, Integer, String, select
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)


class UserDTO(BaseModel):
    id: int
    name: str
    email: str


class UserService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self, user_id: int) -> UserDTO:
        stmt = select(User).where(User.id == user_id)
        result = await self.session.execute(stmt)
        user = result.scalar_one_or_none()
        if user is None:
            raise ValueError("User not found")
        return UserDTO.from_orm(user)

    async def add(self, user: UserDTO) -> None:
        db_user = User(**user.model_dump())
        self.session.add(db_user)
        await self.session.commit()
