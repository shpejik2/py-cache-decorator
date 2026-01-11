from typing import Callable
from typing import Any


def cache(func: Callable) -> Callable:
    results = {}

    def wrapper(*args, **kwargs) -> Any:
        if args in results:
            print("Getting from cache")
            return results[args]
        else:
            print("Calculating new result")
            results[*args] = func(*args, **kwargs)
            return results[args]

    return wrapper
