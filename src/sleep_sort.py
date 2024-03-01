import threading
import time

import numpy as np
from tqdm import tqdm

from execution_time_utils import execution_time_to_real_world

# Define constants
NUMBER_OF_ARRAY_ELEMENTS: int = 100
SORT_TYPE: str = "ascending"
LOW_BOUND: int = 0  # Must be >= 0
HIGH_BOUND: int = 50  # Use small upper bound, otherwise it will run forever


def sleep_sort(array: np.ndarray, sort_type: str = "ascending") -> np.ndarray:
    """
    Runs SleepSort on an array.
    :param array: Input array.
    :param sort_type: Sort type. Default is ascending.
    :return: (np.ndarray) Sorted array.
    """
    sorted_array = []

    def add_to_sorted(value: int, sort_type: str = "ascending") -> None:
        """
        Appends an element to the sorted array after a delay equal to its value.
        :param value: Value to append.
        :param sort_type: Sort type. Default is ascending.
        :return: None.
        """
        if sort_type == "ascending":
            time.sleep(value)
        else:  # descending
            time.sleep(HIGH_BOUND - value)
        sorted_array.append(value)

    # Create a thread for each array element
    threads = [threading.Thread(target=add_to_sorted, args=(value, sort_type)) for value in array]

    # Start all threads
    for thread in threads:
        thread.start()

    # Progress bar
    with tqdm(total=len(threads), desc="Sleep Sort Progress") as pbar:
        for thread in threads:
            thread.join()
            pbar.update(1)

    return np.array(sorted_array)


def main() -> None:
    """
    Main
    :return: None
    """
    # Create a numpy array of n random numbers
    random_array: np.ndarray = np.random.randint(low=LOW_BOUND, high=HIGH_BOUND, size=NUMBER_OF_ARRAY_ELEMENTS)

    print("Original Array:\n", random_array)
    print("--------------------------------")

    # Calculate initial time
    start_time: float = time.time()

    # Run SleepSort
    print(f"Running SleepSort in {SORT_TYPE} order...")
    print("--------------------------------")
    sorted_array = sleep_sort(array=random_array, sort_type=SORT_TYPE)

    print("Sorted Array:", sorted_array)
    print("--------------------------------")

    # Calculate total sorting time
    total_time: float = time.time() - start_time

    # Print execution time to real world metrics
    execution_time_to_real_world(total_time)


if __name__ == '__main__':
    main()
