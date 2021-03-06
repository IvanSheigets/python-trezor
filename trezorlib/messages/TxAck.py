# Automatically generated by pb2py
from .. import protobuf as p
from .TransactionType import TransactionType


class TxAck(p.MessageType):
    MESSAGE_WIRE_TYPE = 22
    FIELDS = {
        1: ('tx', TransactionType, 0),
    }

    def __init__(
        self,
        tx: TransactionType = None
    ) -> None:
        self.tx = tx
