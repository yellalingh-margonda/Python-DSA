# Prints values during the forward (going deeper) recursion phase;
# use this to process or output data before recursive calls.
def print_num_frwd(n, i=1):
    if i > n:
        return
    print(f"i value in forward pass {i}")
    print_num_frwd(n, i + 1)


# Prints values during the backward (unwinding) recursion phase;
# use this to process or output data after all deeper calls complete.
def print_num_backward(n, i=1):
    if i > n:
        return
    print_num_backward(n, i + 1)
    print(f"i value in backward pass {i}")


# Prints values during backward recursion counting down from n to 1;
# use this when recursion decrements and you want post-call processing in descending order.
def print_num_backward_minus(n, i=5):
    if i < 1:
        return
    print_num_backward_minus(n, i - 1)
    print(f"i value in backward pass {i}")


print_num_backward_minus(5)
