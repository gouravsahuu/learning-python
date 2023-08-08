# **Power of Two**: Given an integer, write a function to determine if it is a power of two.
#     - *Input*: 16
#     - *Output*: "True"

import math

def power_of_two(n):
    if n <= 0:
        return False
    return math.log2(n).is_integer()


print(power_of_two(16))
