import json
import logging
from .helper_psql import insert_member


def get_selfdev_members(psql_conn):
    with open(r'..\data_load_project\data\members_enriched.json') as json_file:
        data = json.load(json_file)
        for member in data:
            logging.info(f"Processing member: {member['name']}")
            insert_member(psql_conn,member)


