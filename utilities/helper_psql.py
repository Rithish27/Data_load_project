import psycopg2
import logging

def init_logger():
    """ initialize logger """
    logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info('start of program and logger.')


def psql_connection_test():
    """connect to the PostgreSQL database server"""

    try:
        # connect to the PostgreSQl server
        logging.info('Connecting to the PostgreSQL database...!')
        conn = psycopg2.connect(host='localhost',database='playground',user='postgres',password='admin')

        cur = conn.cursor()

        logging.info('PostgreSQL database version:')
        cur.execute("SELECT version()")

        db_version = cur.fetchone()
        logging.info(db_version)

        cur.close()

    except(Exception,psycopg2.DatabaseError) as error:
        logging.error(error)
    finally:
        if conn is not None:
            conn.close()
            logging.info("database connection closed")


def psql_connection():
    """connect to postgreSQL server"""
    conn = None
    try:
        logging.info('connecting to thr PostgreSQL database...!')
        conn = psycopg2.connect(host='localhost',database='playground',user='postgres',password='<password>')
        return conn
    except (Exception,psycopg2.DatabaseError) as error:
        logging.error(error)

def create_table(psql_conn):
    q_create_table = """
    CREATE TABLE IF NOT EXISTS members(
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        discord_id VARCHAR(255) NOT NULL,
        coding_motivation VARCHAR(255) NOT NULL,
        addiction VARCHAR(255) NOT NULL)
    """

    try:
        cur = psql_conn.cursor()

        cur.execute(q_create_table)
        logging.info(f"Executed query:{q_create_table}")

        cur.close()

        psql_conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)


def insert_member(psql_conn,member):
    q_insert_member = """
    INSERT INTO members(name,discord_id,coding_motivation,addiction)
    VALUES(%s,%s,%s,%s)
    """

    try:
        cur = psql_conn.cursor()
        cur.execute(q_insert_member,(member['name'], member['discord_id'],member['coding_motivation'],member['addiction']))

        psql_conn.commit()

    except (Exception,psycopg2.DatabaseError) as error:
        logging.error(error)
    finally:
        cur.close()
