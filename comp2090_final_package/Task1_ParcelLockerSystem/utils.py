import json
import random
import string
from pathlib import Path


class FeeRecord:
    """Small helper class used to demonstrate the __add__ magic method."""

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
        digits = phone.replace("-", "").strip()
        return digits.isdigit() and len(digits) >= 8

    @staticmethod
    def save_json(path: str, data: dict) -> None:
        file_path = Path(path)
        with file_path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def load_json(path: str) -> dict:
        file_path = Path(path)
        with file_path.open("r", encoding="utf-8") as file:
            return json.load(file)
