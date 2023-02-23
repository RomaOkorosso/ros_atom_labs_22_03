from fastapi import FastAPI
from routes import (
    user_router
)
import uvicorn

app = FastAPI()

app.include_router(user_router)


@app.get("/")
def hello_world():
    return "Hey"


# GET /user/<id>
# POST /user
# PUT /user
# PATCH /user
# DELETE /user/<id>

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
