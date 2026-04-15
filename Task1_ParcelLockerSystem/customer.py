class Customer:
    """Represents a parcel recipient."""

    total_customers = 0

    def __init__(self, name: str, student_id: str, phone: str):
        self._name = name
        self._student_id = student_id
        self._phone = phone
        Customer.total_customers += 1

    @property
    def name(self) -> str:
        return self._name

    @property
    def student_id(self) -> str:
        return self._student_id

    @property
    def phone(self) -> str:
        return self._phone

    def to_dict(self) -> dict:
        return {
            "name": self._name,
            "student_id": self._student_id,
            "phone": self._phone
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Customer":
        return cls(data["name"], data["student_id"], data["phone"])

    def __str__(self) -> str:
        return f"Customer: {self._name} ({self._student_id})"
