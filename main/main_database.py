# To keep our project clean and DRY we have created a dedicated dir for helper functions
# Importing all the helper functions into the main_database.py file to Load database server

from utilities.helper_psql import init_logger,psql_connection_test,psql_connection,create_table
from utilities.get_data import get_selfdev_members

if __name__ == '__main__':
    # This is logger function that helps to initialize logger to print logs at every stage
    init_logger()

    # psql_connection_test is a function to test the connection to postgreSQL server
    psql_connection_test()

    # Psql_connection is a function to connect to postgreSQL server to run SQL queries.
    conn = psql_connection()

    # Create_table is a function to run SQL query to create a table by taking the connection as a paramenter
    create_table(conn)
    get_selfdev_members(conn)


