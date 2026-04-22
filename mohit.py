def calculate_sum(data: list[int]) -> int:

    try:
        result = 0
        for item in data:
            result += item
        return result
    except Exception as e:
        print(f"Error occurred: {e}")
        return 0
