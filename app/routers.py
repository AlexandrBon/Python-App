from fastapi import APIRouter
from contracts import Order
from app.ordering import *
from app.database import orders

router = APIRouter()


@router.post('/mypizza/orders')
async def make_order(
    order: Order
):
    add_order(order)


@router.post('/mypizza/orders/')
async def remove_ordred(
    order: Order
):
    remove_ordred(order)


@router.get('/mypizza/{account_id}')
async def get_order_description(account_id: int):
    return orders[account_id]
