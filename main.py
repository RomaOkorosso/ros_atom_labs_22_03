from fastapi import FastAPI, HTTPException
from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse
from exceptions import ItemNotFound
from routes import user_router, car_router, manufacturer_router
import uvicorn

app = FastAPI()

app.include_router(user_router)
app.include_router(car_router)
app.include_router(manufacturer_router)


@app.exception_handler(ItemNotFound)
def exception_handler(request: Request, exc: ItemNotFound):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND, content={"detail": "Item not found"}
    )


@app.get("/")
def hello_world():
    return "Hey"


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")
