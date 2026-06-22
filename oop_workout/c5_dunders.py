# Challenge 5 - Dunder methods are defined in c1_vehicle.py on the Vehicle base class.
# All subclasses inherit __str__, __repr__, __eq__, __hash__, and __lt__ automatically.
# This file just demonstrates and tests them.

from c3_types import Car, Truck, Motorcycle
from c4_electric import ElectricCar

if __name__ == "__main__":
    c = Car("B-CD-5678", "Toyota", "Yaris", 2023, seats=5)
    print(str(c))
    print(repr(c))

    same_plate = Car("B-CD-5678", "Toyota", "Corolla", 2020)
    print(c == same_plate)   # True

    diff_plate = Car("B-XX-0000", "Toyota", "Yaris", 2023)
    print(c == diff_plate)   # False

    tr = Truck("B-CD-5678", "MAN", "Other", 2000, payload_kg=1)
    print(c == tr)           # True, same plate different class

    tr2 = Truck("B-EF-9012", "MAN", "TGX", 2021, payload_kg=18000)
    print(repr(tr2))

    e = ElectricCar("B-EV-0001", "Tesla", "Model 3", 2024,
                    battery_kwh=60.0, range_km=400)
    print(repr(e))

    # Test sorting by plate
    vehicles = [tr2, c, e]
    for v in sorted(vehicles):
        print(v.plate)

    # Test set deduplication using __hash__ and __eq__
    vehicle_set = {c, same_plate}
    assert len(vehicle_set) == 1, "Same plate should only appear once in a set"
    print("Set dedup test passed.")