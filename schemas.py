from pydantic import BaseModel


class PaymentResponse(BaseModel):
    payment_type: str
    amount: float

    class Config:
        from_attributes = True


class OrderResponse(BaseModel):
    order_id: int
    order_date: str
    menu_name: str
    category: str
    price: float
    quantity: int
    payment_type: str
    payment_amount: float

    class Config:
        from_attributes = True