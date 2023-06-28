# Geometric point configuration polynomials

### Tools for creating a polynomial database well indexed for geometric point configuration problems

#### Only tractable for small primes. For example, when p = 17, the conrresponding table has 10,022,520 rows. There are still many open questions.

The database direcory is initally emtpy, save a blank .gitkeep file.  To initalize and add a table correspoding to your favorite small prime p, navigate to src/ and run

```bash
python3 rows_to_db.py p
```

This will create a table in the file database/maindb.db named "Prime_is_p"

What you do with this information is open ended.  To move an sqlite table to a pandas dataframe, use the sql_to_pandas function in sql_to_pandas.py.
