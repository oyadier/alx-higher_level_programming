
def add_integer(a, b=98):
    """
    Add two numbers and return result

    Args:
        a (int): The first integer value
        b (int): The second integer value

    Return:
        int: The addition of a + b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
