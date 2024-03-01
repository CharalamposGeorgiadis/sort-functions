from time import time

import numpy as np
from IPython.display import clear_output
from numba import njit
from tqdm import tqdm

from execution_time_utils import execution_time_to_real_world

# Define constants
NUMBER_OF_ARRAY_ELEMENTS: int = 12
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
def shuffle(array: np.ndarray) -> None:
    """
    Shuffles a numpy array.
    :param array: Input array.
    :return: None.
    """
    np.random.shuffle(x=array)


def bogo_sort(array: np.ndarray, sort_type: str = "ascending") -> None:
    """
    Runs BogoSort on an array.
    :param array: Input array.
    :param sort_type: Sort type. Default is ascending.
    :return: None.
    """
    # Sort array
    num_shuffles: int = 0
    with tqdm(desc=f"Running BogoSort in {sort_type} order") as pbar:
        while not is_sorted(array=array, sort_type=sort_type):
            shuffle(array=array)
            num_shuffles += 1
            pbar.update(n=1)

    clear_output()
    print("Sorted Array:", array)
    print("Number of Shuffles:", num_shuffles)
    print("--------------------------------")


def main() -> None:
    """
    Main
    :return: None
    """
    # Create a numpy array of n random numbers
    random_array: np.ndarray = np.random.randint(low=LOW_BOUND, high=HIGH_BOUND, size=NUMBER_OF_ARRAY_ELEMENTS)

    print("Original Array:\n", random_array)
    print("--------------------------------")
    clear_output()

    # Calculate initial time
    start_time: float = time()

    # Run BogoSort
    bogo_sort(array=random_array, sort_type=SORT_TYPE)

    # Calculate total sorting time
    total_time: float = time() - start_time

    # Print execution time to real world metrics
    execution_time_to_real_world(total_time)


if __name__ == '__main__':
    main()
