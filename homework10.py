import math

def product_in_range(a, b):
    if a > b:
        a, b = b, a
    product = 1
    for i in range(a, b + 1):
        product *= i
    return product

def max_in_list(lst):
    return max(lst)


def sum_list(lst):
    return sum(lst)


def count_elements(lst):
    even = sum(1 for x in lst if x % 2 == 0)
    odd = sum(1 for x in lst if x % 2 != 0)
    positive = sum(1 for x in lst if x > 0)
    negative = sum(1 for x in lst if x < 0)
    return even, odd, positive, negative

def reverse_list(lst):
    return lst[::-1]

