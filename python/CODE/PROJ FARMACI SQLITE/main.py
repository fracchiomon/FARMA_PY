import sqlite3 as sql
from sqlite3 import Error

id_counter = 0

def connect(db_file):
    """connect to a db"""
    conn = None
    try:
        conn = sql.connect(db_file)
        return conn
    except Error as e:
        print(e)

def create_table(conn, create_table_sql):
    # :param conn: connection object
    # :param create_table_sql: CREATE TABLE statement
    # :return:

    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(e)

def insert_item(conn):

    try:
        c = conn.cursor()
        c.execute("""INSERT INTO farmaci VALUES (?, ?, ?, ?, ?, ?);""", (id, 'Tranquirit gocce', 0, 1, 0, 1))
        conn.commit()
    except Error as e:
        print(e)



def insert_by_user(conn):
    try:
        c = conn.cursor()
        name_insert = input("Inserisci Nome del farmaco:\t")
        q_conf_insert = int(input("Quante compresse per confezione? (0 se gocce)\t"))
        q_day_insert = int(input("Quante compresse/gocce al giorno?\t"))
        est_date_insert = q_conf_insert * q_day_insert
        ssn_insert = int(input("E' coperto dal Servizio Sanitario Nazionale? [1 - Si || 0 - No]\t"))

        c.execute("""INSERT INTO farmaci VALUES (?, ?, ?, ?, ?, ?);""",
                    (id, name_insert, q_conf_insert, q_day_insert, est_date_insert, ssn_insert))

        conn.commit()

        print("Inserimento Avvenuto\n")
    except Error as e:
        print(e)




def delete_item_by_id(conn, id):

    try:
        c = conn.cursor()
        c.execute("DELETE FROM farmaci WHERE id=?", (id,))
        conn.commit()
    except Error as e:
        print(e)

def delete_all_items(conn):

    try:
        c = conn.cursor()
        c.execute("DELETE FROM farmaci;")
    except Error as e:
        print(e)

def print_table(conn):
    try:
        c = conn.cursor()
        c.execute("""SELECT * FROM farmaci;""")
        rows = c.fetchall()
        for row in rows:
            print(row)
        
        conn.commit()
        print("\n")
    except Error as e:
        print(e)

def print_by_id(conn, id):
    try:
        c = conn.cursor()
        c.execute("SELECT * FROM farmaci WHERE id=?;", (id,))
        row = c.fetchone()
        conn.commit()
        print("\n")
    except Error as e:
        print(e)

def main():
    db = r"./DB/farmaci.db"
    

    sql_create_farmaci_table = """ CREATE TABLE IF NOT EXISTS farmaci (
                                        id integer PRIMARY KEY, 
                                        name text NOT NULL,
                                        qty_per_conf integer,  
                                        qty_per_day real NOT NULL, 
                                        estimated_time integer, 
                                        ssn integer NOT NULL
                                        );"""


    conn = connect(db)
    if conn is not None:
        # create table
        create_table(conn, sql_create_farmaci_table)
        #insert_item(conn)
        #print_table(conn)
        #delete_item_by_id(conn, 1)
        print("\n")
        insert_by_user(conn)
        print_table(conn)
        

        conn.close()
    else:
        print("Error! Cannot connect to DB\n\n")
    
    return 0
    

if __name__ == '__main__':
    main()