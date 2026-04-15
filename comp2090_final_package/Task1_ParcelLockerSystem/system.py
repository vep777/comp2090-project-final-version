from __future__ import annotations

from customer import Customer
from locker import Locker
from parcel import ExpressParcel, FragileParcel, StandardParcel
from utils import FeeRecord, SystemUtils


class LockerSystem:
    """Main class that controls customers, parcels, and lockers."""

    def __init__(self, campus_name: str):
        self._campus_name = campus_name
        self._customers: list[Customer] = []
        self._lockers: list[Locker] = []
        self._pickup_codes: dict[str, str] = {}

    @property
    def campus_name(self) -> str:
        return self._campus_name

    def add_customer(self, customer: Customer) -> None:
        if self.find_customer_by_student_id(customer.student_id):
            raise ValueError("This student ID already exists.")
        self._customers.append(customer)

    def add_locker(self, locker: Locker) -> None:
        self._lockers.append(locker)

    def find_customer_by_student_id(self, student_id: str):
        student_id = student_id.strip().upper()
        for customer in self._customers:
            if customer.student_id == student_id:
                return customer
        return None

    def register_parcel(self, parcel_type: str, tracking_id: str, sender: str, recipient: str, weight: float):
        parcel_type = parcel_type.lower().strip()
        if parcel_type == "standard":
            return StandardParcel(tracking_id, sender, recipient, weight)
        if parcel_type == "express":
            return ExpressParcel(tracking_id, sender, recipient, weight)
        if parcel_type == "fragile":
            return FragileParcel(tracking_id, sender, recipient, weight)
        raise ValueError("Unsupported parcel type. Choose standard, express, or fragile.")

    def assign_to_first_available_locker(self, parcel) -> str:
        for locker in self._lockers:
            if locker.is_available and locker.can_fit(parcel):
                locker.assign_parcel(parcel)
                pickup_code = SystemUtils.generate_pickup_code()
                self._pickup_codes[parcel.tracking_id] = pickup_code
                return (
                    f"Assigned {parcel.tracking_id} to {locker.locker_id}.\n"
                    f"Locker size: {locker.size}\n"
                    f"Pickup code: {pickup_code}"
                )
        raise ValueError("No available locker fits this parcel at the moment.")

    def pickup_parcel(self, tracking_id: str, code: str, days_stored: int = 1) -> str:
        tracking_id = tracking_id.strip().upper()
        stored_code = self._pickup_codes.get(tracking_id)
        if stored_code != code.strip().upper():
            raise ValueError("Invalid pickup code.")
        for locker in self._lockers:
            if locker.parcel and locker.parcel.tracking_id == tracking_id:
                parcel = locker.release_parcel()
                storage_fee = FeeRecord(parcel.calculate_fee(days_stored))
                service_fee = FeeRecord(1.5)
                total = storage_fee + service_fee
                del self._pickup_codes[tracking_id]
                return (
                    "Parcel picked up successfully.\n"
                    f"Parcel: {parcel}\n"
                    f"Storage fee: {storage_fee}\n"
                    f"Service fee: {service_fee}\n"
                    f"Total fee: {total}"
                )
        raise ValueError("Parcel not found in any locker.")

    def search_parcel(self, tracking_id: str) -> str:
        tracking_id = tracking_id.strip().upper()
        for locker in self._lockers:
            if locker.parcel and locker.parcel.tracking_id == tracking_id:
                code = self._pickup_codes.get(tracking_id, "N/A")
                return (
                    f"Parcel found in locker {locker.locker_id}.\n"
                    f"Type: {locker.parcel.parcel_type()}\n"
                    f"Recipient: {locker.parcel.recipient}\n"
                    f"Status: {locker.parcel.status}\n"
                    f"Pickup code: {code}"
                )
        return "Parcel is not currently stored in any locker."

    def show_locker_status(self) -> str:
        if not self._lockers:
            return "No lockers in the system."
        return "\n".join(str(locker) for locker in self._lockers)

    def save_data(self, file_path: str = "locker_data.json") -> str:
        data = {
            "campus_name": self._campus_name,
            "customers": [customer.to_dict() for customer in self._customers],
            "lockers": [],
            "pickup_codes": self._pickup_codes,
        }

        for locker in self._lockers:
            locker_data = {
                "locker_id": locker.locker_id,
                "size": locker.size,
                "parcel": locker.parcel.to_dict() if locker.parcel else None,
            }
            data["lockers"].append(locker_data)

        SystemUtils.save_json(file_path, data)
        return f"System data saved to {file_path}."

    @classmethod
    def load_data(cls, file_path: str = "locker_data.json") -> "LockerSystem":
        data = SystemUtils.load_json(file_path)
        system = cls(data["campus_name"])

        for customer_info in data["customers"]:
            system._customers.append(
                Customer(customer_info["name"], customer_info["student_id"], customer_info["phone"])
            )

        for locker_info in data["lockers"]:
            locker = Locker(locker_info["locker_id"], locker_info["size"])
            parcel_info = locker_info["parcel"]
            if parcel_info:
                parcel = system.register_parcel(
                    parcel_info["parcel_type"],
                    parcel_info["tracking_id"],
                    parcel_info["sender"],
                    parcel_info["recipient"],
                    parcel_info["weight"],
                )
                locker.assign_parcel(parcel)
            system.add_locker(locker)

        system._pickup_codes = data.get("pickup_codes", {})
        return system

    @classmethod
    def create_demo_system(cls) -> "LockerSystem":
        system = cls("COMP2090 Smart Locker Hub")
        system.add_locker(Locker("L1", "Small"))
        system.add_locker(Locker("L2", "Medium"))
        system.add_locker(Locker("L3", "Large"))
        system.add_locker(Locker("L4", "Large"))
        system.add_customer(Customer("Alex Chan", "S1001", "91234567"))
        system.add_customer(Customer("Chris Wong", "S1002", "92345678"))
        system.add_customer(Customer("Ivy Lee", "S1003", "93456789"))
        return system
