import pytest

from account import *


class Test:
    def setup_method(self):
        self.p1 = Account('Jane')

    def teardown_method(self):
        del self.p1

    def test_init(self):
        assert self.p1.get_name() == "Jane"
        assert self.p1.get_balance() == 0

    def test_deposit(self):
        assert self.p1.deposit(-10) is False
        assert self.p1.get_balance() == pytest.approx(0, abs=0.001)
        assert self.p1.deposit(-10.50) is False
        assert self.p1.get_balance() == pytest.approx(0, abs=0.001)
        assert self.p1.deposit(0) is False
        assert self.p1.get_balance() == pytest.approx(0, abs=0.001)
        assert self.p1.deposit(10) is True
        assert self.p1.get_balance() == 10
        assert self.p1.deposit(10.50) is True
        assert self.p1.get_balance() == pytest.approx(20.50, abs=0.001)

    def test_withdraw(self):
        assert self.p1.withdraw(0) is False
        assert self.p1.get_balance() == pytest.approx(0, abs=0.001)
        assert self.p1.withdraw(20) is False
        assert self.p1.get_balance() == pytest.approx(0, abs=0.001)
        assert self.p1.withdraw(20.50) is False
        assert self.p1.get_balance() == pytest.approx(0, abs=0.001)
        self.p1.deposit(10)
        assert self.p1.withdraw(2) is True
        assert self.p1.get_balance() == pytest.approx(8, abs=0.001)
        assert self.p1.withdraw(5.5) is True
        assert self.p1.get_balance() == pytest.approx(2.5, abs=0.001)