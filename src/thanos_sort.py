from time import time

import numpy as np
from numba import njit

from execution_time_utils import execution_time_to_real_world

# Define constants
NUMBER_OF_ARRAY_ELEMENTS: int = 100000000
SORT_TYPE: str = "ascending"
LOW_BOUND: int = -2**31 + 1
HIGH_BOUND: int = 2**31 - 1


@njit
def is_sorted(array: np.ndarray, sort_type: str = "ascending") -> bool:
    """
    Checks if a numpy array is sorted.
    :param array: Input array.
    :param sort_type: Sort type. Default is ascending.
    :return: (bool) True if the array is sorted. False otherwise.
    """
    if sort_type == "ascending":
        return bool(np.all(a=array[:-1] <= array[1:]))
    else:  # descending
        return bool(np.all(a=array[:-1] >= array[1:]))


@njit
def thanos_sort(array: np.ndarray, sort_type: str = "ascending") -> np.ndarray:
    """
    Runs ThanosSort on an array.
    :param array: Input array.
    :param sort_type: Sort type. Default is ascending.
    :return: (np.ndarray) Sorted array.
    """
    # End if array has 1 element
    if len(array) == 1:
        return array

    # End if array is sorted
    if is_sorted(array=array, sort_type=sort_type):
        return array

    # Shuffle the array
    np.random.shuffle(array)

    # Take the first half of the shuffled array
    sorted_array = array[:len(array) // 2]

    # Run ThanosSort on the retained half
    return thanos_sort(array=sorted_array, sort_type=sort_type)


def main() -> None:
    """
    Main
    :return: None
    """
    # Create a numpy array of n random numbers
    random_array: np.ndarray = np.random.randint(low=LOW_BOUND, high=HIGH_BOUND, size=NUMBER_OF_ARRAY_ELEMENTS)

    print("Original Array:\n", random_array)
    print("Original Population: ", len(random_array))
    print("--------------------------------")

    # Calculate initial time
    start_time: float = time()

    # Run ThanosSort
    print(f"Running ThanosSort in {SORT_TYPE} order...")
    print("--------------------------------")
    sorted_array = thanos_sort(array=random_array, sort_type=SORT_TYPE)

    print("Sorted Array:\n", sorted_array)
    print("Balanced Population: ", len(sorted_array))
    print("--------------------------------")

    # Calculate total sorting time
    total_time: float = time() - start_time

    # Print execution time to real world metrics
    execution_time_to_real_world(total_time)


if __name__ == '__main__':
    main()
