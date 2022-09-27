from curses.panel import top_panel
from app.contracts import Order
from app.database import orders

def add_order(
    order: Order
    ):
    orders[order.account_id] = Order(order.pizzeria, 
                                  order.name,
                                  order.price, 
                                  order.account_id
                                  )
    return True

def remove_order(
    order: Order
    ):
    del orders[order.account_id]

def get_order_description(
    order: Order
    ):
    return orders[order.account_id]
