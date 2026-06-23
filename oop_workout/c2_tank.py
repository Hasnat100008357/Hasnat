class FuelTank:

    def __init__(self, capacity: float) -> None:
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero.")
        self.__capacity = capacity
        self.__level = 0.0

    def get_level(self) -> float:
        return round(self.__level, 2)

    def get_capacity(self) -> float:
        return self.__capacity

    def fill(self, litres: float) -> None:
        if litres <= 0:
            raise ValueError("Amount to fill must be positive.")
        if self.__level + litres > self.__capacity:
            raise ValueError("This would overflow the tank.")
        self.__level += litres

    def consume(self, litres: float) -> None:
        if litres <= 0:
            raise ValueError("Amount to consume must be positive.")
        if litres > self.__level:
            raise ValueError("Not enough fuel in the tank.")
        self.__level -= litres

    def fill_to_full(self) -> float:
        added = self.__capacity - self.__level
        self.__level = self.__capacity
        return round(added, 2)

    def percent_full(self) -> float:
        return round((self.__level / self.__capacity) * 100, 1)
    