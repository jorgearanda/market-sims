from math import ceil, floor
import secrets


class PrimaryProducer:
    def __init__(
        self,
        name=None,
        units_per_labour_day=1,
        wages_per_labour_day=1,
        free_storage_units=10,
        storage_cost_per_unit_day=0.2,
        credit=10,
        max_labourers=1,
        labourers=1,
        stock=0,
        balance=0,
    ):
        self.name = name if name else secrets.token_hex(8)
        self.units_per_labour_day = units_per_labour_day
        self.wages_per_labour_day = wages_per_labour_day
        self.free_storage_units = free_storage_units
        self.storage_cost_per_unit_day = storage_cost_per_unit_day
        self.credit = credit
        self.max_labourers = max_labourers
        self.labourers = labourers
        self.stock = stock
        self.balance = balance

    def __repr__(self):
        return (
            f"<PrimaryProducer {self.name} "
            + f"({self.labourers} labourers, "
            + f"{self.stock} stock, {self.balance} balance>"
        )

    def tick(self):
        self.labourers = self._labour_force()
        self.stock += self._produce()
        self.stock -= self._dump()
        self.balance -= self._labour_costs() + self._storage_costs()

    def _labour_force(self):
        return min(
            self.max_labourers,
            floor((self.credit + self.balance) / self.wages_per_labour_day),
        )

    def _produce(self):
        return self.labourers * self.units_per_labour_day

    def _dump(self):
        overdraw = ceil(-self.credit - self.balance + self._storage_costs())
        return max(0, overdraw)

    def _labour_costs(self):
        return self.labourers * self.wages_per_labour_day

    def _storage_costs(self):
        overflow = max(0, self.stock - self.free_storage_units)
        return overflow * self.storage_cost_per_unit_day
