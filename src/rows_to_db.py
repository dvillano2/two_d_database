from create_all_rows import all_rows
from pathlib import Path
import sqlite3
import sys

def db_path():
    project_path  = Path().absolute()
    while project_path.name != 'two_d_database':
        project_path = project_path.parent

    return str(project_path / 'database' / 'maindb.db')

def rows_to_db(p):
    ### Prepare sql queries
    ### Userful substrings
    table_name = "Prime_is_{}".format(p)
    poly_params = "size, const_coeff_0, const_coeff_1, const_coeff_2, quad_coeff, unbalanced_dir"
    parallel_sums = "line_sum_0, line_sum_1, line_sum_ud"
    point_sums = "point_sum_{}, " * (p - 1) + "point_sum_{}"
    point_sums = point_sums.format(*tuple(range(p)))
    cols = poly_params + ", " + parallel_sums + ", " + point_sums
    placeholders = ', '.join('?' * (9 + p))

    ### Queries
    sql_check = "SELECT name FROM sqlite_master WHERE type='table' AND name='{}'".format(table_name)
    sql_create_table = ("CREATE TABLE " + table_name + " (" + cols + " INTEGER)").replace(",", " INTEGER,")
    sql_insert = "INSERT INTO {} ({}) VALUES ({})".format(table_name, cols, placeholders)

    ### Execute queries
    conn = sqlite3.connect(db_path())
    cur = conn.cursor()

    cur.execute(sql_check)
    exists = cur.fetchone()
        
    if exists is None:
        cur.execute(sql_create_table)
        cur.executemany(sql_insert, all_rows(p))
        conn.commit()
    else:
        print ("Prime_is_{} already exists in the db".format(p))

    cur.close()
    conn.close()

if __name__ == "__main__":
    p = int(sys.argv[1])
    rows_to_db(p)
