from fastapi import FastAPI

from app.api.routes import api_router


app = FastAPI()

app.include_router(api_router)


@app.get("/")
async def hello():
    return {"message": "FastAPI"}


# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}