#!/usr/bin/python3
"""
states models
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    db_host = "localhost"
    db_user = sys.argv[1]  # "your_username"
    db_password = sys.argv[2]  # "your_password"
    db_name = sys.argv[3]  # "your_database_name"
    port = 3306
    state_name = sys.argv[4]  # "your_database_name"
    query = "SELECT name FROM cities WHERE state_id = \
(SELECT id FROM states WHERE name LIKE BINARY %s) ORDER BY cities.id ASC"
    params = (state_name,)
    db = MySQLdb.connect(
        host=db_host, user=db_user, passwd=db_password, db=db_name, port=port
    )
    cursor = db.cursor()

    cursor.execute(query, params)
    rows = cursor.fetchall()
    tuples = ()
    for row in rows:
        tuples += row
    print(*tuples, sep=", ")

    cursor.close()
    db.close()
