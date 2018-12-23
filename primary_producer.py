import secrets


class PrimaryProducer():
    def __init__(
        self,
        name=None,
        labour_per_day=1,
        free_storage_units=10,
        extra_storage_per_unit_day=0.2,
        credit=10,
        labourers=1,
        stock=0,
        cash_on_hand=0,
        balance=0,
    ):
        self.name = name if name else secrets.token_hex(8)
        self.labour_per_day = labour_per_day
        self.free_storage_units = free_storage_units
        self.extra_storage_per_unit_day = extra_storage_per_unit_day
        self.credit = credit
        self.labourers = labourers
        self.stock = stock
        self.cash_on_hand = cash_on_hand
        self.balance = balance

    def __repr__(self):
        return f'<PrimaryProducer {self.name} ' + \
            f'({self.labourers} labourers, ' + \
            f'{self.stock} stock, {self.cash_on_hand} cash, ' + \
            f'{self.balance} balance>'
