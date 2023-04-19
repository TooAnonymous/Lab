from account import *


class Test:
    def setup_method(self):
        self.p1 = Account('Jane')

    def teardown_method(self):
        del self.p1

    def test_deposit(self):
        assert self.p1.deposit(10) is True