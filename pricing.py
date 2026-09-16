import math
from abc import ABC, abstractmethod

HOURLY_RATES = {
    "motorcycle": 50,
    "car": 100,
    "bus": 200,
}

FLAT_RATES = {
    "motorcycle": 100,
    "car": 200,
    "bus": 400,
}

class PricingStrategy(ABC):
    @abstractmethod
    def calculate_fee(self, duration_minutes: int, vehicle_type: str) -> float:
        pass

class HourlyPricing(PricingStrategy):
    def calculate_fee(self, duration_minutes: int, vehicle_type: str) -> float:
        rate = HOURLY_RATES[vehicle_type]
        hours = max(1, math.ceil(duration_minutes / 60))
        return float(hours * rate)

class FlatPricing(PricingStrategy):
    def calculate_fee(self, duration_minutes: int, vehicle_type: str) -> float:
        return float(FLAT_RATES[vehicle_type])

def create_pricing(pricing_type: str) -> PricingStrategy:
    if pricing_type == "hourly":
        return HourlyPricing()
    elif pricing_type == "flat":
        return FlatPricing()
    else:
        raise ValueError("Pricing must be hourly or flat")
    