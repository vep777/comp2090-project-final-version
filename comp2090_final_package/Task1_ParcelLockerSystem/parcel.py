from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import datetime


class Parcel(ABC):
    """Abstract parcel class shared by all parcel types."""

    total_parcels = 0
    BASE_DAILY_FEE = 2.0

    def __init__(self, tracking_id: str, sender: str, recipient: str, weight: float):
        if not self.validate_tracking_id(tracking_id):
            raise ValueError("Tracking ID must start with 'P' and contain at least 5 characters.")
        if float(weight) <= 0:
            raise ValueError("Weight must be greater than 0.")

        self._tracking_id = tracking_id.strip().upper()
        self._sender = sender.strip()
        self._recipient = recipient.strip()
        self._weight = float(weight)
        self._status = "Waiting for locker assignment"
        self._created_at = datetime.now()
        Parcel.total_parcels += 1

    @property
    def tracking_id(self) -> str:
        return self._tracking_id

    @property
    def sender(self) -> str:
        return self._sender

    @property
    def recipient(self) -> str:
        return self._recipient

    @property
    def weight(self) -> float:
        return self._weight

    @property
    def status(self) -> str:
        return self._status

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @property
    def required_locker_size(self) -> str:
        """A simple size rule based on weight for a beginner-level project."""
        if self._weight <= 1.0:
            return "Small"
        if self._weight <= 3.0:
            return "Medium"
        return "Large"

    def update_status(self, new_status: str) -> None:
        self._status = new_status

    @staticmethod
    def validate_tracking_id(tracking_id: str) -> bool:
        return isinstance(tracking_id, str) and tracking_id.upper().startswith("P") and len(tracking_id.strip()) >= 5

    @classmethod
    def get_total_parcels(cls) -> int:
        return cls.total_parcels

    @abstractmethod
    def calculate_fee(self, days_stored: int) -> float:
        raise NotImplementedError

    @abstractmethod
    def parcel_type(self) -> str:
        raise NotImplementedError

    def to_dict(self) -> dict:
        return {
            "parcel_type": self.parcel_type().lower(),
            "tracking_id": self._tracking_id,
            "sender": self._sender,
            "recipient": self._recipient,
            "weight": self._weight,
            "status": self._status,
            "created_at": self._created_at.isoformat(timespec="seconds"),
        }

    def __str__(self) -> str:
        return (
            f"{self.parcel_type()} Parcel | ID: {self._tracking_id} | Recipient: {self._recipient} "
            f"| Weight: {self._weight:.1f}kg | Status: {self._status}"
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Parcel):
            return False
        return self._tracking_id == other._tracking_id


class StandardParcel(Parcel):
    RATE_MULTIPLIER = 1.0

    def parcel_type(self) -> str:
        return "Standard"

    def calculate_fee(self, days_stored: int) -> float:
        return round(days_stored * self.BASE_DAILY_FEE * self.RATE_MULTIPLIER, 2)


class ExpressParcel(Parcel):
    RATE_MULTIPLIER = 1.8

    def parcel_type(self) -> str:
        return "Express"

    def calculate_fee(self, days_stored: int) -> float:
        return round(days_stored * self.BASE_DAILY_FEE * self.RATE_MULTIPLIER + 5, 2)


class FragileParcel(Parcel):
    RATE_MULTIPLIER = 1.4
    PROTECTION_FEE = 3.0

    def parcel_type(self) -> str:
        return "Fragile"

    def calculate_fee(self, days_stored: int) -> float:
        return round(days_stored * self.BASE_DAILY_FEE * self.RATE_MULTIPLIER + self.PROTECTION_FEE, 2)
