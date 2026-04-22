def calculate_sum(data: list[int]) -> int:
    """
    This function calculates the sum of a list of integers.
    It demonstrates proper error handling and clean structure.
    """
    try:
        result = 0
        for item in data:
            result += item
        return result
    except Exception as e:
        print(f"Error occurred: {e}")
        return 0
