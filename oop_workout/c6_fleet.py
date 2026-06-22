from c1_vehicle import Vehicle
from c3_types import Car, Truck, Motorcycle
from c4_electric import ElectricCar
import json


class Fleet:

    def __init__(self, name: str) -> None:
        self.name = name
        self._vehicles: dict[str, Vehicle] = {}

    def add(self, vehicle: Vehicle) -> None:
        if vehicle.plate in self._vehicles:
            raise ValueError(f"A vehicle with plate {vehicle.plate} is already in the fleet.")
        self._vehicles[vehicle.plate] = vehicle

    def remove(self, plate: str) -> None:
        if plate not in self._vehicles:
            raise KeyError(f"No vehicle with plate {plate} found.")
        del self._vehicles[plate]

    def find(self, plate: str) -> Vehicle | None:
        return self._vehicles.get(plate, None)

    def total_kilometres(self) -> int:
        return sum(v.kilometres for v in self._vehicles.values())

    def drive_all(self, km: int) -> tuple[list, list]:
        successes = []
        failures = []
        for plate, vehicle in self._vehicles.items():
            try:
                vehicle.drive(km)
                successes.append(plate)
            except ValueError as e:
                failures.append((plate, str(e)))
        return successes, failures

    def cars_only(self) -> list:
        # isinstance is acceptable here because the method's whole purpose
        # is to filter by type. In print_summary we want polymorphic behaviour
        # so isinstance would be the wrong tool there.
        return [v for v in self._vehicles.values() if isinstance(v, Car)]

    def average_kilometres(self) -> float:
        # Returns 0.0 for an empty fleet to avoid division by zero
        if not self._vehicles:
            return 0.0
        return self.total_kilometres() / len(self._vehicles)

    def save(self, path: str) -> None:
        data = []
        for v in self._vehicles.values():
            entry = {
                "type": type(v).__name__,
                "plate": v.plate,
                "make": v.make,
                "model": v.model,
                "year": v.year,
                "kilometres": v.kilometres,
            }
            if isinstance(v, Car):
                entry["seats"] = v.seats
            elif isinstance(v, Truck):
                entry["payload_kg"] = v.payload_kg
            elif isinstance(v, ElectricCar):
                entry["battery_kwh"] = v.battery_kwh
                entry["range_km"] = v.range_km
            data.append(entry)
        with open(path, "w") as f:
            json.dump({"name": self.name, "vehicles": data}, f, indent=2)

    @classmethod
    def load(cls, path: str) -> "Fleet":
        with open(path, "r") as f:
            data = json.load(f)
        fleet = cls(data["name"])
        type_map = {
            "Car": Car,
            "Truck": Truck,
            "Motorcycle": Motorcycle,
            "ElectricCar": ElectricCar,
        }
        for entry in data["vehicles"]:
            vtype = entry["type"]
            plate = entry["plate"]
            make = entry["make"]
            model = entry["model"]
            year = entry["year"]
            if vtype == "Car":
                v = Car(plate, make, model, year, seats=entry.get("seats", 5))
            elif vtype == "Truck":
                v = Truck(plate, make, model, year, payload_kg=entry["payload_kg"])
            elif vtype == "Motorcycle":
                v = Motorcycle(plate, make, model, year)
            elif vtype == "ElectricCar":
                v = ElectricCar(plate, make, model, year,
                                battery_kwh=entry["battery_kwh"],
                                range_km=entry["range_km"])
            else:
                continue
            v.kilometres = entry.get("kilometres", 0)
            fleet.add(v)
        return fleet

    def __len__(self) -> int:
        return len(self._vehicles)

    def __iter__(self):
        return iter(self._vehicles.values())

    def __contains__(self, plate: str) -> bool:
        return plate in self._vehicles

    def __str__(self) -> str:
        return f"Fleet '{self.name}': {len(self)} vehicle(s)"


def print_summary(fleet: Fleet) -> None:
    print("=== FLEET REPORT ===")
    print(fleet)
    print(f"Total kilometres: {fleet.total_kilometres()}")
    print("-" * 20)
    for vehicle in fleet:
        print(vehicle)
    print("=" * 20)