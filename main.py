from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

#This is comment
#Path Parameter with type
@app.get('/gashity/{id}')
async def get_list(id:int):
    return {"The id number is:":id}