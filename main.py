from fastapi import FastAPI
from enum import Enum


class EnumName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}


# This is comment
# Path Parameter with type
@app.get("/gashity/{id}")
async def get_list(id: int):
    return {"The id number is:": id}


@app.get("/holiday/{id}")
async def employee_detail(id: int):
    return {"This holiday is: ": id}


@app.get("/awdamet/{id}")
async def employee_detail(id: int):
    return {"Melkam Awdamet": id}


@app.get("/meskerem/{id}")
async def employee_detail(id: int):
    return {"This is Ethiopian New Year": id}


####The following is creating Enums
@app.get("/models/{model_name}")
async def get_model(model_name: EnumName):
    if model_name is EnumName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


###The foloowing is using query parameters
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/gashity/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]
