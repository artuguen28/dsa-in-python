
def binarySearch(lst: list, value: int) -> int:
    """
    Algorithm Analysis:

    Time Complexity: 
        Best Case: 
            O(1): Occurs when the value is found at the middle index in the first iteration.
        Worst Case:
            O(log n): In each iteration, the search space is halved, so the number of iterations is 
            logarihmic where (n) in the size of the list.
        Average Case:
            O(log n): Logarithmic time due to the halving of the search space.

    Space Complexity:
        O(1): The function uses a constant amount of extra space (left, right, middle) regardless of
        the size of the input list. 

    """

    # Use left and right indexes to limit the search space
    left, right = 0, len(lst) - 1

    while left <= right:
        middle = (left + right) // 2

        if lst[middle] == value:
            return middle
        elif lst[middle] < value:
            print(f"{value} is greater than {lst[middle]} -> left: {left} | right: {right}")
            left = middle + 1
        else:
            print(f"{value} is smaller than {lst[middle]} -> left: {left} | right: {right}")
            right = middle - 1

    return -1

if __name__ == "__main__":
    lst = [2, 5, 6, 19, 30, 43, 45, 56, 62, 74, 82, 100, 103]
    value = 63
    result = binarySearch(lst, value)
    if result != -1:
        print(f"Value {value} found at index {result}.")
    else:
        print(f"Value {value} not found in the list.")
