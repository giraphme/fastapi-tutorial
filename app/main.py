from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def get_item(item_id: int):
    return {"item_id": item_id}


@app.get("/users/me")
async def get_user_me():
    return {"user_id": 0}


@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id}


@app.get("/users/{user_id}/items/{item_id}")
async def get_user_item(user_id: int, item_id: int, skip: int = 0, limit: int | None = None):
    return {"user_id": user_id, "item_id": item_id, "skip": skip, "limit": limit}
