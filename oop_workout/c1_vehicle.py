class Vehicle:
    fleet_size = 0

    def __init__(self, plate: str, make: str, model: str, year: int) -> None:
        self.plate = plate
        self.make = make
        self.model = model
        self.year = year
        self.kilometres = 0
        Vehicle.fleet_size += 1

    def drive(self, km: int) -> None:
        if km <= 0:
            raise ValueError("Distance must be a positive number.")
        self.kilometres += km

    def describe(self) -> str:
        return f"{self.year} {self.make} {self.model} ({self.plate})"

    def service_due(self) -> bool:
        return self.kilometres > 15000

    def __str__(self) -> str:
        return self.describe()

    def __repr__(self) -> str:
        return f"{type(self).__name__}('{self.plate}', '{self.make}', '{self.model}', {self.year})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vehicle):
            return NotImplemented
        return self.plate == other.plate

    def __hash__(self) -> int:
        return hash(self.plate)

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Vehicle):
            return NotImplemented
        return self.plate < other.plate