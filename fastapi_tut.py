from fastapi import FastAPI
from enum import Enum
app = FastAPI()
'''
@app.get("/hello/{name}")

async def hello(name):
    return f"welcome to fastAPI tut {name}"
'''
class AvailableCuisines(str,Enum):
    indian = 'indian'
    american = 'american'
    italian = 'italian' 
    
food_items = {
    'indian': ['Samosa','Dosa'],
    'american':['Hot Dog','Apple pie'],
    'italian':['Ravioli','Pizza']
}

# in browser : http://127.0.0.1:8000/get_items/indian
# output : [
#  "Samosa",
#  "Dosa"]

@app.get("/get_items/{cuisine}")

async def get_items(cuisine:AvailableCuisines):
    return food_items.get(cuisine)