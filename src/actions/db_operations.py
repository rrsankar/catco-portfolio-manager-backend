import mariadb


def validate_user(uname, password):

    config = {
        'user': 'root',
        'password': 'root',
        'host': '127.0.0.1',
        'port': 3306,
        'database': 'catco'
    }

    # connection for MariaDB.
    connection = mariadb.connect(**config)
    # create a connection cursor.
    cursor = connection.cursor()
    # execute a SQL statement.
    cursor.execute(f"SELECT * FROM credentials WHERE uname='{uname}' AND password='{password}';")
    # Get all output.
    output = cursor.fetchall()
    # Close the cursor.
    cursor.close()

    if output:
        return 1
    else:
        return 0
