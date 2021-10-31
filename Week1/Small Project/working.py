from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from fastapi.param_functions import Query
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None
    
class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None

inventory={}

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, description="The ID of the item you'd like to view:", gt=0)):
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item name not found.")

@app.get("/get-by-name")
def get_item(*, item_id:int, name: Optional[str] = None, test: int):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item name not found.")

@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Item ID already exists.")
    
    inventory[item_id] = item 
    return inventory[item_id]

@app.put("/update-item/{item_id}")
def create_item(item_id: int, item: UpdateItem):
    if item_id in inventory:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Item ID does not exist.")
    
    if item.name != None:
        inventory[item_id].name = item.name

    if item.price != None:
        inventory[item_id].price = item.price 

    if item.brand != None:
        inventory[item_id].brand = item.brand 
        
    return inventory[item_id]

@app.delete("/delete-item")
def delete_item(item_id: int = Query(..., description="The ID of the item that needs to be deleted:")):
    if item_id not in inventory:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Item ID does not exist.")
    
    del inventory[item_id]
    return {"Success": "Item deleted!"}