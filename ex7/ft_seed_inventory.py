def ft_seed_inventory(seed_type: str, qty: int, unit: str) -> None:
    seed_type = seed_type.capitalize()

    if unit == "packets":
        print(f"{seed_type} seeds: {qty} {unit} available")
    elif unit == "grams":
        print(f"{seed_type} seeds: {qty} {unit} total")
    elif unit == "area":
        print(f"{seed_type} seeds: covers {qty} square meters")
    else:
        print("Unknown unit type")
