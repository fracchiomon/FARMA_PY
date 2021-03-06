import sqlite3 as sql
from sqlite3 import Error
import sys

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



def insert_by_user(conn):
    try:
        c = conn.cursor()
        name_insert = input("Inserisci Nome del farmaco:\t")
        q_conf_insert = int(input("Quante compresse per confezione? (0 se gocce)\t"))
        q_day_insert = float(input("Quante compresse/gocce al giorno? [inserire quantità con decimi (es: 2.5)]\t"))
        est_date_insert = q_conf_insert // q_day_insert
        ssn_insert = int(input("E' coperto dal Servizio Sanitario Nazionale? [1 - Si || 0 - No]\t"))
        
        

        c.execute("""INSERT INTO farmaci VALUES (?, ?, ?, ?, ?);""",
                    (name_insert, q_conf_insert, q_day_insert, est_date_insert, ssn_insert))

        conn.commit()

        print("Inserimento Avvenuto\n")
    except Error as e:
        print("\n")
        print(e)




def delete_item_by_name(conn, name):

    try:
        c = conn.cursor()
        c.execute("DELETE FROM farmaci WHERE name=?", (name,))
        conn.commit()
        
        print("Inserimento Avvenuto\n")
    except Error as e:
        print("\n")
        print(e)


def print_table(conn):
    try:
        c = conn.cursor()
        c.execute("""SELECT * FROM farmaci;""")
        rows = c.fetchall()
        print("\n")
        for row in rows:
            print(row)
        
        conn.commit()
        print("\n")
    except Error as e:
        print("\n")
        print(e)

def print_by_name(conn, name):
    try:
        c = conn.cursor()
        c.execute("SELECT * FROM farmaci WHERE name=?;", (name,))
        row = c.fetchone()
        print("\n")
        print(row)
        conn.commit()
        print("\n")
    except Error as e:
        print(e)
        
def flush_db(conn):
    print("\nSEI SICURO DI VOLER CANCELLARE TUTTI GLI ELEMENTI DEL DB?\n")
    choice = input("[y/n]\t")
    if choice == 'y':
        try:

            c = conn.cursor()
            c.execute("DELETE FROM farmaci;")
        except Error as e:
            print(e)
    elif choice == 'n':
        return
    else:
        print("\nINPUT NON CORRETTO.")
        return
    
def menu():
    print("Benvenuto, digita la tua scelta:\n")
    print("1:\tInserisci nuovo elemento nel DB")
    print("2:\tElimina elemento dal DB")
    print("3:\tStampa DB")
    print("4:\tStampa elemento del DB\n")
    print("\n-1:\tDistruggi DB (ATTENZIONE)")
    print("0:\tESCI")
    
    scelta = -3
    while (scelta != -2):
        scelta = int(input("\nCosa vuoi fare?\t"))
        if ((scelta < 0 and scelta != -2 and scelta != -1) or (scelta > 4)):
            print("INPUT NON CORRETTO, RIPROVA\n")
            continue
        else:
            break
    return scelta