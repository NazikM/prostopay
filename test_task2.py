import unittest

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from task2 import Base, UserDTO, User, UserService


class TestUserService(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = create_async_engine("sqlite+aiosqlite:///:memory:")
        cls.async_session = async_sessionmaker(cls.engine, class_=AsyncSession)

    @classmethod
    def tearDownClass(cls):
        cls.engine.dispose()

    async def setUp(self):
        async with self.__class__.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        self.session = await self.async_session()

    async def tearDown(self):
        await self.session.close()

    async def test_get_existing_user(self):
        # Create a test user in the database
        user_data = {"id": 1, "name": "Nazar", "email": "marusinnazar@gmail.com"}
        user_dto = UserDTO(**user_data)
        db_user = User(**user_dto.model_dump())
        self.session.add(db_user)
        await self.session.commit()

        # Instantiate the UserService with the test session
        service = UserService(self.session)

        # Call the get method with the test user's ID
        result = await service.get(user_data["id"])

        # Assert that the returned UserDTO matches the test user's data
        self.assertEqual(result.model_dump(), user_data)

    async def test_get_nonexistent_user(self):
        # Instantiate the UserService with an empty session
        service = UserService(self.session)

        # Call the get method with a nonexistent user's ID
        with self.assertRaises(ValueError):
            await service.get(999)

    async def test_add_user(self):
        # Instantiate the UserService with an empty session
        service = UserService(self.session)

        # Create a new UserDTO instance to add to the database
        new_user_data = {"id": 1, "name": "Nazar", "email": "marusinnazar@gmail.com"}
        new_user_dto = UserDTO(**new_user_data)

        # Call the add method to add the new user to the database
        await service.add(new_user_dto)

        # Query the database to check if the new user was added successfully
        stmt = select(User).where(User.id == new_user_data["id"])
        result = await self.session.execute(stmt)
        db_user = result.scalar_one_or_none()

        # Assert that the added user exists in the database and has correct data
        self.assertIsNotNone(db_user)
        self.assertEqual(db_user.name, new_user_data["name"])
