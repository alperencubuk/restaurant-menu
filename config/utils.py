def str_to_bool(value: str) -> bool:
    return str(value).lower() in {"true", "1", "t", "y", "yes"}


def str_to_tuple(value: str, separator: str = ",") -> tuple:
    return tuple(item.strip() for item in str(value).split(separator))
