# x^n = (x^(n/2))^2
#x^n = x * (x^((n - 1) / 2))^2
# 2^8 = (2^4)^2
#      = ((2^2)^2)^2
#      = (((2^1)^2)^2)^2
#
# → 2^1 = 2
# → 2^2 = 2 * 2 = 4
# → 2^4 = 4 * 4 = 16
# → 2^8 = 16 * 16 = 256

def power(x, n):
    """
    Calculates x raised to the power of n (x^n).

    Args:
        x (float or int): The base.
        n (int): The exponent. Can be positive, negative, or zero.

    Returns:
        float: The result of x^n.
    """
    if n == 0:
        return 1.0  # Any number to the power of 0 is 1.0 (float for consistency)

    if n < 0:
        # For negative exponents, x^n = 1 / x^(-n)
        # We make the recursive call with a positive exponent
        return 1.0 / power(x, -n)

    # Base case for positive n: if n is 1, return x
    # This prevents infinite recursion for n=1 when n//2 is 0
    if n == 1:
        return x

    # Recursive step (Divide and Conquer - Exponentiation by Squaring)
    half_power = power(x, n // 2)  # Calculate x^(n/2)

    if n % 2 == 0:
        # If n is even, x^n = (x^(n/2))^2
        return half_power * half_power
    else:
        # If n is odd, x^n = x * (x^(n/2))^2
        return x * half_power * half_power

def power_2(x,n):
    if n<=1:
        return 1
    return x*power_2(x, n-1)
