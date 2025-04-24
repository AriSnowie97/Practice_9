from typing import Callable, Iterable, TypeVar, Mapping, Any, List, Tuple, Dict
from collections.abc import Sequence

T = TypeVar('T')
U = TypeVar('U')
K = TypeVar('K')
V = TypeVar('V')

def process_data(data: Iterable[T], operation: Callable[[T], U]) -> Iterable[U]:
    if not callable(operation):
            # Replacing the invalid operation with a valid one
        invalid_operation = process_data([1, 2], lambda x: x * 2)
        print(f"Valid operation (doubled values): {invalid_operation}")

    try:
        if isinstance(data, list):
            return [operation(item) for item in data]
        elif isinstance(data, tuple):
            return tuple(operation(item) for item in data)
        elif isinstance(data, dict):
            return {key: operation(value) for key, value in data.items()}
        elif isinstance(data, Sequence):
            return type(data)(operation(item) for item in data)
        elif isinstance(data, Iterable):
            return (operation(item) for item in data)
        else:
            raise TypeError(f"Collection type '{type(data).__name__}' is not supported.")
    except Exception as e:
        return f"Data processing error: {e}"

def filter_data(data: Iterable[T], predicate: Callable[[T], bool]) -> Iterable[T]:
    if not callable(predicate):
        raise TypeError("Argument 'predicate' must be a function.")
    try:
        if isinstance(data, list):
            return [item for item in data if predicate(item)]
        elif isinstance(data, tuple):
            return tuple(item for item in data if predicate(item))
        elif isinstance(data, dict):
            return {key: value for key, value in data.items() if predicate(value)}
        elif isinstance(data, Sequence):
            return type(data)(item for item in data if predicate(item))
        elif isinstance(data, Iterable):
            return (item for item in data if predicate(item))
        else:
            raise TypeError(f"Collection type '{type(data).__name__}' is not supported.")
    except Exception as e:
        return f"Data filtering error: {e}"

def combine_values(*args: Any, separator: str = "", start_value: Any = None) -> Any:
    if not args:
        return start_value if start_value is not None else ""
    first_type = type(args[0])
    result = start_value if start_value is not None else args[0]
    try:
        for i in range(1, len(args)):
            current_arg = args[i]
            if type(current_arg) == first_type:
                if first_type in (int, float):
                    result += current_arg
                elif first_type == str:
                    result += separator + current_arg
                else:
                    return "Error: Unsupported type for combination."
            else:
                return "Error: Argument types are not the same."
        return result
    except TypeError as e:
        return f"Value combination error: {e}"

def multiply_by_two(x: int) -> int:
    return x * 2

def is_even(x: int) -> bool:
    return x % 2 == 0

def get_length(s: str) -> int:
    return len(s)

if __name__ == "__main__":

    numbers = [1, 2, 3, 4, 5]
    doubled_numbers = process_data(numbers, multiply_by_two)
    print(f"Doubled numbers: {doubled_numbers}")

    names = ("Alice", "Bob", "Charlie")
    lengths = process_data(names, get_length)
    print(f"Name lengths: {lengths}")

    info = {"a": 10, "b": 20, "c": 30}
    doubled_info = process_data(info, multiply_by_two)
    print(f"Doubled dictionary values: {doubled_info}")

    even_numbers = filter_data(numbers, is_even)
    print(f"Even numbers: {even_numbers}")

    long_names = filter_data(names, lambda x: len(x) > 3)
    print(f"Long names: {long_names}")

    even_info = filter_data(info, lambda x: x > 15)
    print(f"Dictionary values greater than 15: {even_info}")

    sum_result = combine_values(1, 2, 3, 4, start_value=0)
    print(f"Sum of numbers: {sum_result}")

    combined_string = combine_values("Hello", "World", separator=" ")
    print(f"Combined string: {combined_string}")

    mixed_combine = combine_values(1, "a")
    print(f"Mixed type combination attempt: {mixed_combine}")

    invalid_operation = process_data([1, 2], "not_a_function")
    print(f"Invalid operation: {invalid_operation}")

    mixed_sum = combine_values(1, 2, "a")
    print(f"Attempt to sum with string: {mixed_sum}")