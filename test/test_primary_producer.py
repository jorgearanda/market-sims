from pytest import approx

from primary_producer import PrimaryProducer


class TestDefaultPrimaryProducer:
    def setup(self):
        self.p = PrimaryProducer()

    def tick_many(self, times):
        for _ in range(times):
            self.p.tick()

    def test_instantiates(self):
        assert True

    def test_default_values(self):
        assert self.p.name is not None
        assert self.p.labourers == 1
        assert self.p.stock == 0
        assert self.p.balance == 0

    def test_repr(self):
        assert "PrimaryProducer" in str(self.p)

    def test_tick(self):
        self.p.tick()
        assert self.p.stock == 1
        assert self.p.balance == -1

    def test_pay_for_storage(self):
        self.p.balance = 10
        self.tick_many(11)
        assert self.p.stock == 11
        assert self.p.balance == -1.2

    def test_run_out_of_credit(self):
        self.tick_many(10)

        # At the edge
        assert self.p.labourers == 1
        assert self.p.stock == 10
        assert self.p.balance == -10

        self.p.tick()
        assert self.p.labourers == 0
        assert self.p.stock == 10
        assert self.p.balance == -10

    def test_dump_deadbeat_storage(self):
        self.p.balance = 2
        self.tick_many(11)

        # Close to the edge
        assert self.p.labourers == 1
        assert self.p.stock == 11
        assert self.p.balance == -9.2

        self.tick_many(4)
        assert self.p.labourers == 0
        assert self.p.stock == 11
        assert self.p.balance == approx(-10)

        self.p.tick()
        assert self.p.stock == 10
        assert self.p.balance == approx(-10)
