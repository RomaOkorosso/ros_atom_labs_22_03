from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
import schemas
from database import get_db
from services import UserService, car_service, ManufacturerService

router = APIRouter(prefix="/user", tags=["user"])
car_router = APIRouter(prefix="/car", tags=["car"])
manufacturer_router = APIRouter(prefix="/man", tags=["manufacturer"])


@router.post("/")
async def create_new_user(
    new_user: schemas.UserCreate, db: AsyncSession = Depends(get_db)
) -> schemas.User:
    return UserService.create_user(db=db, new_user=new_user)


@router.patch("/<user_id>")
async def update_user(
    user_id: int, user: schemas.UserUpdate, db: AsyncSession = Depends(get_db)
) -> schemas.User:
    return UserService.update(db=db, obj=user, obj_id=user_id)


@car_router.post("/")
async def create_new_car(
    new_car: schemas.CarCreate, db: AsyncSession = Depends(get_db)
) -> schemas.CarInDB:
    return await car_service.create_car(db=db, new_car=new_car)


@car_router.patch("/<car_id>")
async def update_car(
    car_id: int, car: schemas.CarUpdate, db: AsyncSession = Depends(get_db)
) -> schemas.CarInDB:
    return await car_service.update(db=db, obj=car, obj_id=car_id)


@car_router.get("/<car_id>")
async def get_car(car_id: int, session: AsyncSession = Depends(get_db)) -> schemas.CarInDB:
    return await car_service.select_one(session=session, obj_id=car_id)


@manufacturer_router.post("/")
async def create_new_manufacturer(
    new_man: schemas.ManufacturerCreate, db: AsyncSession = Depends(get_db)
) -> schemas.ManufacturerInDB:
    return ManufacturerService.create(db=db, new_man=new_man)


@manufacturer_router.patch("/<man_id>")
async def update_man(
    man_id: int, man: schemas.ManufacturerUpdate, db: AsyncSession = Depends(get_db)
) -> schemas.ManufacturerInDB:
    return ManufacturerService.update(db=db, obj=man, obj_id=man_id)
