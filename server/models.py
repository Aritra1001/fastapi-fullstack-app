from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int

    # this is the constructor so that I can use Product class elsewhere
    # def __init__(self, id: int, name: str, description: str, price: float, quantity: int):
    #     self.id = id
    #     self.name = name
    #     self.description = description
    #     self.price = price
    #     self.quantity = quantity

    # pydantic is used for data validation. Like converting from server side to JSON format to send it to the client