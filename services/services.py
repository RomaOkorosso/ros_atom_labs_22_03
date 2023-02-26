from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
import exceptions
import schemas
import database
from exceptions import ItemNotFound


class CarService:
    model = database.Car

    async def select_one(self, session: AsyncSession, obj_id: int) -> database.Car:
        car: Result = await session.execute(select(self.model).where(self.model.id == obj_id))
        car: database.Car = car.scalar_one_or_none()

        if not car:
            raise exceptions.ItemNotFound()

        return car

    @staticmethod
    async def create_car(db: AsyncSession, new_car: schemas.CarCreate) -> database.Car:
        new_car = database.Car(**new_car.dict())
        db.add(new_car)
        await db.commit()
        await db.refresh(new_car)
        return new_car

    @staticmethod
    async def update(db: AsyncSession, obj: schemas.CarUpdate, obj_id: int) -> database.Car:
        db_obj = await car_service.select_one(session=db, obj_id=obj_id)

        if not db_obj:
            raise ItemNotFound

        for k, v in obj.dict().items():
            if v is not None:
                setattr(db_obj, k, v)

        await db.commit()
        await db.refresh(db_obj)
        return db_obj


car_service = CarService()


class UserService:
    @staticmethod
    def create_user(db: AsyncSession, new_user: schemas.UserCreate):
        new_user = database.User(**new_user.dict())
        db.add(new_user)
        db.commit()
        return new_user

    @staticmethod
    def update(db: AsyncSession, obj: schemas.UserUpdate, obj_id: int) -> database.User:
        db_obj = db.query(database.User).get(obj_id)  # noqa
        if not db_obj:
            raise ItemNotFound

        for k, v in obj.dict().items():
            if v is not None:
                setattr(db_obj, k, v)

        db.commit()
        return db_obj


class ManufacturerService:
    @staticmethod
    def create(db: AsyncSession, new_man: schemas.ManufacturerCreate):
        new_man = database.Manufacturer(**new_man.dict())
        db.add(new_man)
        db.commit()
        return new_man

    @staticmethod
    def update(
            db: AsyncSession, obj: schemas.ManufacturerUpdate, obj_id: int
    ) -> database.Manufacturer:
        db_obj = db.query(database.Manufacturer).get(obj_id)  # noqa
        if not db_obj:
            raise ItemNotFound

        for k, v in obj.dict().items():
            if v is not None:
                setattr(db_obj, k, v)

        db.commit()
        return db_obj
