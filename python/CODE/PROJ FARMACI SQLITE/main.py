import sqlite3 as sql
from sqlite3 import Error
import sys
import db_funcs

id_counter = 0

# def connect(db_file):
#     """connect to a db"""
#     conn = None
#     try:
#         conn = sql.connect(db_file)
#         return conn
#     except Error as e:
#         print(e)

# def create_table(conn, create_table_sql):
#     # :param conn: connection object
#     # :param create_table_sql: CREATE TABLE statement
#     # :return:

#     try:
#         c = conn.cursor()
#         c.execute(create_table_sql)
#         conn.commit()
#     except Error as e:
#         print(e)



# def insert_by_user(conn):
#     try:
#         c = conn.cursor()
#         name_insert = input("Inserisci Nome del farmaco:\t")
#         q_conf_insert = int(input("Quante compresse per confezione? (0 se gocce)\t"))
#         q_day_insert = float(input("Quante compresse/gocce al giorno? [inserire quantità con decimi (es: 2.5)]\t"))
#         est_date_insert = q_conf_insert // q_day_insert
#         ssn_insert = int(input("E' coperto dal Servizio Sanitario Nazionale? [1 - Si || 0 - No]\t"))
        
        

#         c.execute("""INSERT INTO farmaci VALUES (?, ?, ?, ?, ?);""",
#                     (name_insert, q_conf_insert, q_day_insert, est_date_insert, ssn_insert))

#         conn.commit()

#         print("Inserimento Avvenuto\n")
#     except Error as e:
#         print("\n")
#         print(e)




# def delete_item_by_name(conn, name):

#     try:
#         c = conn.cursor()
#         c.execute("DELETE FROM farmaci WHERE name=?", (name,))
#         conn.commit()
        
#         print("Inserimento Avvenuto\n")
#     except Error as e:
#         print("\n")
#         print(e)


# def print_table(conn):
#     try:
#         c = conn.cursor()
#         c.execute("""SELECT * FROM farmaci;""")
#         rows = c.fetchall()
#         print("\n")
#         for row in rows:
#             print(row)
        
#         conn.commit()
#         print("\n")
#     except Error as e:
#         print("\n")
#         print(e)

# def print_by_name(conn, name):
#     try:
#         c = conn.cursor()
#         c.execute("SELECT * FROM farmaci WHERE name=?;", (name,))
#         row = c.fetchone()
#         print("\n")
#         print(row)
#         conn.commit()
#         print("\n")
#     except Error as e:
#         print(e)
        
# def flush_db(conn):
#     print("\nSEI SICURO DI VOLER CANCELLARE TUTTI GLI ELEMENTI DEL DB?\n")
#     choice = input("[y/n]\t")
#     if choice == 'y':
#         try:

#             c = conn.cursor()
#             c.execute("DELETE FROM farmaci;")
#         except Error as e:
#             print(e)
#     elif choice == 'n':
#         return
#     else:
#         print("\nINPUT NON CORRETTO.")
#         return
        
# def menu():
#     print("Benvenuto, digita la tua scelta:\n")
#     print("1:\tInserisci nuovo elemento nel DB")
#     print("2:\tElimina elemento dal DB")
#     print("3:\tStampa DB")
#     print("4:\tStampa elemento del DB\n")
#     print("\n-1:\tDistruggi DB (ATTENZIONE)")
#     print("0:\tESCI")
    
#     scelta = -3
#     while (scelta != -2):
#         scelta = int(input("\nCosa vuoi fare?\t"))
#         if ((scelta < 0 and scelta != -2 and scelta != -1) or (scelta > 4)):
#             print("INPUT NON CORRETTO, RIPROVA\n")
#             continue
#         else:
#             break
#     return scelta
    

def main():
    db = r"./DB/farmaci.db"
    conn = db_funcs.connect(db)
    

    sql_create_farmaci_table = """ CREATE TABLE IF NOT EXISTS farmaci (
                                         
                                        name text NOT NULL,
                                        qty_per_conf integer,  
                                        qty_per_day real NOT NULL, 
                                        estimated_time integer, 
                                        ssn integer
                                        );"""


    
    if conn is not None:

        db_funcs.create_table(conn, sql_create_farmaci_table)

        scelta2 = 1
        
        while (scelta2 == 1):
            scelta = db_funcs.menu()
            if scelta == 1:
                db_funcs.insert_by_user(conn)
            elif scelta == 2:
                elimina = input("Inserisci il Nome (attenzione alle maiuscole) dell'oggetto da eliminare:\t")
                db_funcs.delete_item_by_name(conn, elimina)
            elif scelta == 3:
                db_funcs.print_table(conn)
            elif scelta == 4:
                stampa = input("Inserisci il Nome (attenzione alle maiuscole) dell'oggetto da stampare:\t")
                db_funcs.print_by_name(conn, stampa)
            elif scelta == -1:
                db_funcs.flush_db(conn)
            elif scelta == 0:
                conn.close()
                sys.exit(69)
            else:
                pass
            
            print("\nVuoi effettuare altre operazioni?\nDigita 1 per tornare al menu, 0 per uscire.\n")
            scelta2 = int(input())
            if scelta2 == 1:
                continue
            elif scelta2 == 0:
                break
            else:
                print("\nINPUT NON VALIDO.")
                
            
        conn.close()
    else:
        print("Error! Cannot connect to DB\n\n")
    
    return 0
    

if __name__ == '__main__':
    main()
