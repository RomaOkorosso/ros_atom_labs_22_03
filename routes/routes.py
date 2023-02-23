from datetime import datetime

from fastapi import APIRouter, Depends
import schemas
import database

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/<user_id>")
def get_user_by_id(user_id: int) -> schemas.User:
    return schemas.User(id=user_id,
                        name="asdf",
                        email="asdf@fakemail.com",
                        age=10,
                        gender=database.GenderEnum.male,
                        created_at=datetime.now(),
                        updated_at=datetime.now())
