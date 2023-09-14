from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel

class Report(BaseModel):
    start_date:str
    description:str
    quantity:int
    unit_price:float|None=None

class Student(BaseModel):
    first_name:str
    last_name:str
    age:int
    sex:str
    year:int|None=None

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

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


#Post Request Body
@app.post('/reports')
async def create_report(report:Report):
    return report


@app.post('/students')
async def create_stdent(student:Student):
    return  student

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict