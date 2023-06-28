from poly_to_rows import poly_to_rows
from itertools import product

def all_rows(p):
    row_list = []
    for unbal_dir in range(2, p):
        for coeffs in product(range(p), range(p), range(p), range(p)):
            coeffs = list(coeffs)
            row_list += poly_to_rows(p, unbal_dir, coeffs)
    return row_list
