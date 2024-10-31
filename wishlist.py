from fastapi import FastAPI


app = FastAPI()


wishlist: list[dict] = []


@app.get('/wish')
async def get_all_wishes():
    return wishlist



@app.get('/wish/{wish_id}')
async def get_wish(wish_id: int):
    for wish in wishlist:
        if wish["id"] == wish_id:
            return wish
        else:
           return {"message": "ID not found"}
    return {"message": "Wishlist is empty"}



@app.post('/wish')
async def create_wish(id: int, title: str, description: str):
    wish_for_create = {
        "id": id,
        "title": title,
        "description": description
    }
    wishlist.append(wish_for_create)
    return wishlist



@app.put("/wish/{id}")
async def update_wish(id: int, title: str = None, description: str = None):
    for wish in wishlist:
        if wish["id"] == id:
            if title:
                wish["title"] = title
            if description:
                wish["description"] = description
        else:
            return {"message": "ID not found"}
    return {"message": "Wishlist is empty"}



@app.delete('/wish/{id}')
async def delete_wish(id: int):
    for wish in wishlist:
        if wish["id"] == id:
            wishlist.remove(wish)
            return {"message": "Wish deleted."}
        return {"message": "ID not found"}
    return {"message": "Wishlist is empty"}



@app.delete('/wish')
async def delete_all_wishes():
    wishlist = []
    return wishlist