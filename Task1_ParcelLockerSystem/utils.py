import random
import string


class FeeRecord:
    """A simple class to demonstrate magic method __add__."""

    def __init__(self, amount: float):
        self.amount = float(amount)

    def __add__(self, other: "FeeRecord") -> "FeeRecord":
        return FeeRecord(self.amount + other.amount)

    def __str__(self) -> str:
        return f"HK${self.amount:.2f}"


class SystemUtils:
    @staticmethod
    def generate_pickup_code(length: int = 6) -> str:
        letters = string.ascii_uppercase + string.digits
        return "".join(random.choice(letters) for _ in range(length))

    @staticmethod
    def validate_phone(phone: str) -> bool:
        digits = phone.replace("-", "")
        return digits.isdigit() and len(digits) >= 8
