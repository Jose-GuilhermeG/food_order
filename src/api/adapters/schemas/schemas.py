from pydantic import BaseModel


class FoodListSerializer(BaseModel):
    name : str
    slug : str
    description : str
    price : float
