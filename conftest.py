from class_data import Bank
import pytest
import dataclasses

@pytest.fixture()
def bank() -> Bank:
    bank = Bank(name="Ploy",stakeholders=["Jack"], capital=MIN_CAPITAL)
    return bank


@pytest.fixture()
def bank_creation_payload() -> Bank:
    payload = {"name": "Poly", "stakeholders": "Jack", "capital": MIN_CAPITAL }
    return bank