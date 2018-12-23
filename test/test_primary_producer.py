from primary_producer import PrimaryProducer


class TestDefaultPrimaryProducer():
    def setup(self):
        self.p = PrimaryProducer()

    def test_instantiates(self):
        assert True

    def test_default_values(self):
        assert self.p.name is not None
        assert self.p.labourers == 1
        assert self.p.stock == 0
        assert self.p.cash_on_hand == 0
        assert self.p.balance == 0

    def test_repr(self):
        assert 'PrimaryProducer' in str(self.p)
