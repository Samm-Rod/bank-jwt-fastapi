import enum

class TransactionType(enum.Enum):
    deposit = "deposit"
    withdraw = "withdraw"
    transfer = "transfer"
    pix = "pix"