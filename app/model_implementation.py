from contracts import Pizzeria


class Order:
    def __init__(
        self,
        pizzeria: Pizzeria,
        name: str,
        price: float,
        account_id: int
        ):
        self.pizzeria = pizzeria
        self.name = name
        self.price = price
        self.account_id = account_id
              