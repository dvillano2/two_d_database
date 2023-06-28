import sqlite3
import pandas as pd
from rows_to_db import db_path

### Find non-sqare mod p
def q_nr(p):
    qnr = 2
    e = (p - 1) // 2
    while pow(qnr, e, p) == 1:
        qnr += 1
    return qnr

### Generate sql query
def geo_sql(p):
    table_name = "Prime_is_{}".format(p)
    point_sums = ("point_sum_{}, " * (p - 1) + "point_sum_{}").format(*tuple(range(p)))
    lines = "line_sum_0 = line_sum_1 AND line_sum_0 = line_sum_ud AND line_sum_0 = {} * size".format(p)
    points0 = "MAX({}) <= {} + MIN({})".format(point_sums, p, point_sums)
    full_sum = point_sums.replace(",", " +")
    points1 = "MIN({}) = 3 * size - (({}) - {} * MIN({})) / {}".format(point_sums, full_sum, p, point_sums, p)
    qnr = "quad_coeff IN (1, {})".format(q_nr(p))

    return "SELECT * FROM {} WHERE {} AND {} AND {} AND {}".format(table_name, lines, points0, points1, qnr)

### Function that exracts geometric subset of polynomial table to pandas for analysis
def sql_to_pandas(p):
    table_name = "Prime_is_{}".format(p)
    sql_check = "SELECT name FROM sqlite_master WHERE type='table' AND name='{}'".format(table_name)

    conn = sqlite3.connect(db_path())
    cur = conn.cursor()

    cur.execute(sql_check)
    exists = cur.fetchone()

    if exists is None:
        print ("No table for {}".format(p))
        return

    sql = geo_sql(p)
    df = pd.read_sql_query(sql, conn)

    cur.close()
    conn.close()

    return df
