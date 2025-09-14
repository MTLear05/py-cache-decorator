from typing import Callable, Any


def cache(func: Callable) -> Callable:
    final_list = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        if args in final_list:
            print("Getting from cache")
            return final_list[args]
        print("Calculating new result")
        result = func(*args)
        final_list[args] = result
        return result
    return wrapper
