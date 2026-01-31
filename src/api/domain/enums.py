from enum import Enum

class OrderStatus(Enum): 
    PENDING = "Pendente" 
    CONFIRMED = "Confirmado" 
    DELIVERED = "Entregue" 
    CANCELED = "Cancelado"