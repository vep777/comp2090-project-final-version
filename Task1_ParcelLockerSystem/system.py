from __future__ import annotations

import json
from pathlib import Path

from customer import Customer
from locker import Locker
from parcel import ExpressParcel, FragileParcel, StandardParcel
from utils import FeeRecord, SystemUtils


class LockerSystem:
    """Main class coordinating customers, parcels, and lockers."""

    DATA_FILE = "locker_data.json"

    def __init__(self, campus_name: str):
        self._campus_name = campus_name
        self._customers: list[Customer] = []
        self._lockers: list[Locker] = []
        self._pickup_codes: dict[str, str] = {}

    @property
    def campus_name(self) -> str:
        return self._campus_name

    def add_customer(self, customer: Customer) -> None:
        for existing_customer in self._customers:
            if existing_customer.student_id.lower() == customer.student_id.lower():
                raise ValueError("Customer with the same student ID already exists.")
        self._customers.append(customer)

    def add_locker(self, locker: Locker) -> None:
        self._lockers.append(locker)

    def register_parcel(self, parcel_type: str, tracking_id: str, sender: str, recipient: str, weight: float):
        parcel_type = parcel_type.lower()
        if parcel_type == "standard":
            return StandardParcel(tracking_id, sender, recipient, weight)
        if parcel_type == "express":
            return ExpressParcel(tracking_id, sender, recipient, weight)
        if parcel_type == "fragile":
            return FragileParcel(tracking_id, sender, recipient, weight)
        raise ValueError("Unsupported parcel type. Choose standard, express, or fragile.")

    def get_required_locker_size(self, weight: float) -> str:
        if weight <= 1:
            return "Small"
        if weight <= 3:
            return "Medium"
        return "Large"

    def assign_to_first_available_locker(self, parcel) -> str:
        required_size = self.get_required_locker_size(parcel.weight)
        size_order = {"Small": 1, "Medium": 2, "Large": 3}
        required_rank = size_order[required_size]

        for locker in self._lockers:
            locker_rank = size_order.get(locker.size, 3)
            if locker.is_available and locker_rank >= required_rank:
                locker.assign_parcel(parcel)
                pickup_code = SystemUtils.generate_pickup_code()
                self._pickup_codes[parcel.tracking_id] = pickup_code
                return (
                    f"Assigned {parcel.tracking_id} to {locker.locker_id} ({locker.size}). "
                    f"Pickup code: {pickup_code}"
                )

        raise ValueError("No suitable available locker for this parcel.")

    def pickup_parcel(self, tracking_id: str, code: str, days_stored: int = 1) -> str:
        tracking_id = tracking_id.upper()
        stored_code = self._pickup_codes.get(tracking_id)
        if stored_code != code:
            raise ValueError("Invalid pickup code.")

        for locker in self._lockers:
            if locker.parcel and locker.parcel.tracking_id == tracking_id:
                parcel = locker.release_parcel()
                fee = FeeRecord(parcel.calculate_fee(days_stored))
                service_fee = FeeRecord(1.5)
                total = fee + service_fee
                del self._pickup_codes[tracking_id]
                return (
                    f"Parcel picked up successfully.\n"
                    f"Parcel: {parcel}\n"
                    f"Storage fee: {fee}\n"
                    f"Service fee: {service_fee}\n"
                    f"Total fee: {total}"
                )
        raise ValueError("Parcel not found in any locker.")

    def find_parcel(self, tracking_id: str) -> str:
        tracking_id = tracking_id.upper()

        for locker in self._lockers:
            if locker.parcel and locker.parcel.tracking_id == tracking_id:
                pickup_code = self._pickup_codes.get(tracking_id, "N/A")
                return (
                    f"Parcel found.\n"
                    f"Tracking ID: {locker.parcel.tracking_id}\n"
                    f"Type: {locker.parcel.parcel_type()}\n"
                    f"Recipient: {locker.parcel.recipient}\n"
                    f"Status: {locker.parcel.status}\n"
                    f"Locker ID: {locker.locker_id}\n"
                    f"Pickup code: {pickup_code}"
                )

        return "Parcel not found in any locker."

    def show_locker_status(self) -> str:
        if not self._lockers:
            return "No lockers in the system."
        return "\n".join(str(locker) for locker in self._lockers)

    def save_data(self, filename: str | None = None) -> str:
        target_file = filename or self.DATA_FILE
        data = {
            "campus_name": self._campus_name,
            "customers": [customer.to_dict() for customer in self._customers],
            "lockers": [],
            "pickup_codes": self._pickup_codes
        }

        for locker in self._lockers:
            locker_data = {
                "locker_id": locker.locker_id,
                "size": locker.size,
                "parcel": locker.parcel.to_dict() if locker.parcel else None
            }
            data["lockers"].append(locker_data)

        with open(target_file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        return f"Data saved successfully to {target_file}."

    @classmethod
    def load_data(cls, filename: str | None = None) -> "LockerSystem":
        target_file = filename or cls.DATA_FILE
        file_path = Path(target_file)

        if not file_path.exists():
            raise ValueError(f"Save file {target_file} does not exist.")

        with open(target_file, "r", encoding="utf-8") as file:
            data = json.load(file)

        system = cls(data["campus_name"])

        for customer_data in data.get("customers", []):
            system._customers.append(Customer.from_dict(customer_data))

        for locker_data in data.get("lockers", []):
            locker = Locker(locker_data["locker_id"], locker_data["size"])
            parcel_data = locker_data.get("parcel")

            if parcel_data:
                parcel = system.register_parcel(
                    parcel_data["parcel_type"],
                    parcel_data["tracking_id"],
                    parcel_data["sender"],
                    parcel_data["recipient"],
                    parcel_data["weight"]
                )
                parcel.update_status(parcel_data["status"])
                locker.assign_parcel(parcel)

            system._lockers.append(locker)

        system._pickup_codes = data.get("pickup_codes", {})
        return system

    @classmethod
    def create_demo_system(cls) -> "LockerSystem":
        system = cls("COMP2090 Smart Locker Hub")
        system.add_locker(Locker("L1", "Small"))
        system.add_locker(Locker("L2", "Medium"))
        system.add_locker(Locker("L3", "Large"))
        system.add_customer(Customer("Alex Chan", "s1001", "91234567"))
        system.add_customer(Customer("Chris Wong", "s1002", "92345678"))
        return system
