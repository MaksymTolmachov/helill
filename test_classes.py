import pytest
from class_data import Bank, MIN_CAPITAL

class TestBank:

    def test_bank_creation_too_low_capital(self):
        with pytest.raises(ValueError):
            Bank(name="3456",stakeholders=[], capital=MIN_CAPITAL - 1 )


    def test_bank_add_one_stakeholders(self):
        bank = Bank(name="Ploy",stakeholders=["Jack"], capital=MIN_CAPITAL)
        assert len(bank.stakeholders) == 1














