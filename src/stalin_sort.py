from time import time

import numpy as np
from numba import njit

from execution_time_utils import execution_time_to_real_world

# Define constants
NUMBER_OF_ARRAY_ELEMENTS: int = 1000000000
SORT_TYPE: str = "ascending"
LOW_BOUND: int = -2**31 + 1
HIGH_BOUND: int = 2**31 - 1


@njit
def stalin_sort(array: np.ndarray, sort_type: str = "ascending") -> np.ndarray:
    """
    Runs StalinSort on an array.
    :param array: Input array.
    :param sort_type: Sort type. Default is ascending.
    :return: (np.ndarray) Sorted array.
    """
    # Sort array
    sorted_list = [array[0]]
    for element in array[1:]:
        if sort_type == "ascending":
            if element >= sorted_list[-1]:
                sorted_list.append(element)
        else:  # descending
            if element <= sorted_list[-1]:
                sorted_list.append(element)

    return np.array(sorted_list)


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

    # Run StalinSort
    print(f"Running StalinSort in {SORT_TYPE} order...")
    print("--------------------------------")
    sorted_array = stalin_sort(array=random_array, sort_type=SORT_TYPE)

    print("Sorted Array:\n", sorted_array)
    print("Cleansed Population: ", len(sorted_array))
    print("--------------------------------")

    # Calculate total sorting time
    total_time: float = time() - start_time

    # Print execution time to real world metrics
    execution_time_to_real_world(total_time)


if __name__ == '__main__':
    main()
