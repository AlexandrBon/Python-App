from pydantic import BaseModel


class Pizzeria(BaseModel):
    """Pizzeria description"""

    name:  str
    city:  str
    steet: str


class Order(BaseModel):
    """Pizza description"""

    pizzeria: Pizzeria
    name: str
    
    price: float
    account_id: int
