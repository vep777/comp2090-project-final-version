class Locker:
    """Represents one physical locker slot."""

    total_lockers = 0

    def __init__(self, locker_id: str, size: str):
        self._locker_id = locker_id.strip().upper()
        self._size = size.strip().title()
        self._parcel = None
        Locker.total_lockers += 1

    @property
    def locker_id(self) -> str:
        return self._locker_id

    @property
    def size(self) -> str:
        return self._size

    @property
    def parcel(self):
        return self._parcel

    @property
    def is_available(self) -> bool:
        return self._parcel is None

    def can_fit(self, parcel) -> bool:
        size_rank = {"Small": 1, "Medium": 2, "Large": 3}
        return size_rank[self._size] >= size_rank[parcel.required_locker_size]

    def assign_parcel(self, parcel) -> None:
        if not self.is_available:
            raise ValueError(f"Locker {self._locker_id} is already occupied.")
        if not self.can_fit(parcel):
            raise ValueError(f"Locker {self._locker_id} is too small for parcel {parcel.tracking_id}.")
        self._parcel = parcel
        parcel.update_status(f"Stored in locker {self._locker_id}")

    def release_parcel(self):
        if self.is_available:
            raise ValueError(f"Locker {self._locker_id} is already empty.")
        parcel = self._parcel
        self._parcel = None
        parcel.update_status("Picked up")
        return parcel

    def __str__(self) -> str:
        status = "Available" if self.is_available else f"Occupied by {self._parcel.tracking_id}"
        return f"Locker {self._locker_id} ({self._size}) - {status}"
