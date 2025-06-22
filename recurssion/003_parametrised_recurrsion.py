# 🔢 Sum of first n natural numbers using recursion

# ✅ Method 1: Parametrized recursion (prints the result directly)
def sum_parametrized(n, total=0):
    """
    Prints the sum of first n numbers using parameter-passing recursion.

    Args:
        n (int): The current number.
        total (int): The cumulative sum (default is 0).
    """
    if n < 1:
        print(f"Total (parametrized): {total}")
        return
    sum_parametrized(n - 1, total + n)


# Call
sum_parametrized(3)


# ✅ Method 2: Functional recursion (returns the result)
def sum_return(n, total=0):
    """
    Returns the sum of first n numbers using return-based recursion.

    Args:
        n (int): The current number.
        total (int): The cumulative sum (default is 0).

    Returns:
        int: Total sum from 1 to n.
    """
    if n < 1:
        return total
    return sum_return(n - 1, total + n)


# Call and print
total = sum_return(3)
print(f"Total (return-based): {total}")

def sum_recursive(n):
    """
    Recursively returns the sum of all numbers from n down to 0.

    Args:
        n (int): The number to start summing from.

    Returns:
        int: The total sum from 0 to n.
    """
    if n < 0:
        return 0
    return n + sum_recursive(n - 1)

# Example usage
print(f"Total sum (0 to 3): {sum_recursive(3)}")

def factorial(n):
    if n<=1:
        return 1
    return n* factorial(n-1)
print(f"Factorial of 3 is {factorial(4)}")
