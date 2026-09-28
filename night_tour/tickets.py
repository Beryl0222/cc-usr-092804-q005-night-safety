"""夜游订单与容量核算。"""
from dataclasses import dataclass
from decimal import Decimal
@dataclass
class TicketOrder:
    order_id: str; capacity: int; paid: Decimal; status: str = 'paid'; refunded: Decimal = Decimal('0')
class TicketBook:
    def __init__(self): self.orders = {}
    def add(self, order): self.orders[order.order_id] = order
    def cancel(self, order_id, amount):
        order = self.orders[order_id]
        if order.status == 'cancelled': return order
        order.status = 'cancelled'; order.refunded += Decimal(str(amount)); return order
    def capacity(self): return sum(o.capacity for o in self.orders.values() if o.status != 'cancelled')
    def revenue(self): return sum((o.paid - o.refunded for o in self.orders.values()), Decimal('0'))
    def audit(self): return [{'id': o.order_id, 'status': o.status, 'refunded': str(o.refunded)} for o in self.orders.values()]
