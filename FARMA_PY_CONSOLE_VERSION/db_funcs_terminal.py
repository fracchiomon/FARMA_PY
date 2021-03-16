import sqlite3 as sql
from sqlite3 import Error



def connect(db_file):
    """connect to a db"""
    conn = None
    try:
        conn = sql.connect(db_file)
        return conn
    except Error as e:
        print(e)


def create_table(conn, create_table_sql):
    """creazione tabella con la sql_table passata dal main"""

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
    """Inserimento dall'utente (FARMA_PY: CONSOLE)"""

    try:
        c = conn.cursor()
        name_insert = input("Inserisci Nome del farmaco:\t")
        q_conf_insert = int(
            input("Quante compresse per confezione? (0 se gocce)\t"))
        q_day_insert = float(input(
            "Quante compresse/gocce al giorno? [inserire quantità con decimi (es: 2.5)]\t"))
        est_date_insert = q_conf_insert // q_day_insert
        ssn_insert = int(
            input("E' coperto dal Servizio Sanitario Nazionale? [1 - Si || 0 - No]\t"))

        c.execute("""INSERT INTO farmaci VALUES (?, ?, ?, ?, ?);""",
                  (name_insert, q_conf_insert, q_day_insert, est_date_insert, ssn_insert))

        conn.commit()

        print("\nInserimento Avvenuto\n")
    except Error as e:
        print("\n")
        print(e)


def insert_item(conn, name, q_conf, q_day, ssn):
    """(FARMA_PY: GUI) - Inserimento dall'utente mediante Entry box della libreria Tk:\n
    Il valore 'Durata Stimata' (est variable nella funzione) è dato da una basilare stima approssimata"""
    try:
        c = conn.cursor()

        # catch dell'errore "divisione per 0" -> se denominatore = 0 => est = 0
        if float(q_day) == 0:
            est = 0
        else:
            est = int(q_conf) // float(q_day)

        # passaggio nella tabella dei valori opportunamente convertiti
        c.execute("""INSERT INTO farmaci VALUES (?, ?, ?, ?, ?);""",
                  (name, int(q_conf), float(q_day), int(est), int(ssn)))

        conn.commit()

        print("\nInserimento Avvenuto!\n")
    except Error as e:
        print("\n")
        print(e)


def delete_item_by_name(conn, name):
    """Cancellazione di un item scelto dall'User tramite il nome"""

    try:
        c = conn.cursor()

        # esecuzione comando
        c.execute("DELETE FROM farmaci WHERE name=?", (name,))
        conn.commit()

        print("\nCancellazione Avvenuta!\n")
    except Error as e:
        print("\n")
        print(e)


def print_table(conn):
    """( conn=sqlite3.connect )\n
    Stampa della tabella "Farmaci";
    rows immagazzina il fetchall() della tabella, successivamente tramite\n
    un for loop viene iterato e i valori stampati\n
    e poi inseriti in una nuova lista che viene riportata"""
    try:
        c = conn.cursor()
        c.execute("""SELECT * FROM farmaci;""")
        # effettuo il fetch dei valori dalla tabella
        rows = c.fetchall()
        rows_list = []
        print("\n")
        for row in rows:
            print(row)
            rows_list.append(row)

        conn.commit()
        print("\n")
        # rows_list è mandata in return per essere riusata a piacere
        return rows_list
    except Error as e:
        print("\n")
        print(e)


def print_by_name(conn, name):
    """(conn=sqlite3.connect , name=String)\n
    Stampa un solo elemento a scelta dalla tabella.\n
    Si usa il fetchone e non il fetchall."""
    try:
        c = conn.cursor()
        c.execute("SELECT * FROM farmaci WHERE name=?;", (name,))
        row = c.fetchone()
        print("\n")
        print(row)
        conn.commit()
        print("\n")
        # return di row per eventuale riutilizzo
        return row
    except Error as e:
        print("\n")
        print(e)


def flush_db(conn):
    """( conn=sqlite3.connect )\n
    Elimina tutta la tabella dopo aver chiesto conferma."""

    print("\nSEI SICURO DI VOLER CANCELLARE TUTTI GLI ELEMENTI DEL DB?\n")
    choice = input("[y/N]\t")
    if choice == 'y':
        try:

            c = conn.cursor()
            c.execute("DELETE FROM farmaci;")
            print("\nIl Database è stato distrutto correttamente.\n")
        except Error as e:
            print(e)

    # il No è l'opzione predefinita
    elif (choice == 'n' or choice == 'N'):
        return
    else:
        print("\nINPUT NON CORRETTO.\nCancellazione fallita.\n")
        return


def menu():
    print("Benvenuto, digita la tua scelta:\n")
    print("1:\tInserisci nuovo elemento nel DB")
    print("2:\tElimina elemento dal DB")
    print("3:\tStampa DB")
    print("4:\tStampa elemento del DB\n")
    print("\n-1:\tDistruggi DB (ATTENZIONE)")
    print("0:\tESCI")

    # controllo del valore di Scelta
    scelta = -3
    while (scelta != -2):
        scelta = int(input("\nCosa vuoi fare?\t"))
        if ((scelta < 0 and scelta != -2 and scelta != -1) or (scelta > 4)):
            print("INPUT NON CORRETTO, RIPROVA\n")
            continue
        else:
            break
    return scelta
