import psycopg2
from flask_sqlalchemy import SQLAlchemy
from psycopg2 import pool

# from model import Mission

db = SQLAlchemy




CONNECTION_BOOL = psycopg2.pool.SimpleConnectionPool(
    minconn=1,
    maxconn=10,
    database='missions_wwii',
    user='postgres',
    password='8520',
    host = 'localhost',
    port = '5432'
)


def get_db_connection():
    if CONNECTION_BOOL:
        con = CONNECTION_BOOL.getconn()
        return con


def release_db_connection(connection):
    CONNECTION_BOOL.putconn(connection)