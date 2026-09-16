VEHICLE_TYPES = {"motorcycle", "car", "bus"}

VEHICLE_RULES = {
    "motorcycle": {
        "prefix": "M",
        "spots_required": 1,
    },
    "car": {
        "prefix": "C",
        "spots_required": 1,
    },
    "bus": {
        "prefix": "B",
        "spots_required": 2,
    },
}

def validate_vehicle_type(vehicle_type: str) -> None:
    if vehicle_type not in VEHICLE_TYPES:
        raise ValueError(
            f"Invalid vehicle type: {vehicle_type}"
        )

def spots_required(vehicle_type: str) -> int:
    validate_vehicle_type(vehicle_type)
    return VEHICLE_RULES[vehicle_type]["spots_required"]

def spot_prefix(vehicle_type: str) -> str:
    validate_vehicle_type(vehicle_type)
    return VEHICLE_RULES[vehicle_type]["prefix"]


