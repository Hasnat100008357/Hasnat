from c1_vehicle import Vehicle


class ElectricCar(Vehicle):

    def __init__(self, plate: str, make: str, model: str, year: int,
                 battery_kwh: float, range_km: float) -> None:
        super().__init__(plate, make, model, year)
        self.battery_kwh = battery_kwh
        self.range_km = range_km
        self.__charge = 0.0

    def get_charge(self) -> float:
        return round(self.__charge, 2)

    def charge(self, kwh: float) -> None:
        if kwh <= 0:
            raise ValueError("Charge amount must be positive.")
        if self.__charge + kwh > self.battery_kwh:
            raise ValueError("This would exceed the battery capacity.")
        self.__charge += kwh

    def drive(self, km: int) -> float:
        """Uses battery charge to drive. Raises ValueError if not enough charge."""
        needed = self.battery_kwh * km / self.range_km
        if needed > self.__charge:
            raise ValueError("Not enough charge for this trip.")
        self.__charge -= needed
        super().drive(km)
        return round(needed, 2)

    def describe(self) -> str:
        return super().describe() + ", electric car"


def drive_all(vehicles: list, km: int) -> list:
    results = []
    for v in vehicles:
        results.append(v.drive(km))
    return results