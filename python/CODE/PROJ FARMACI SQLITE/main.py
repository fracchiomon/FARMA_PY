import sqlite3 as sql
from sqlite3 import Error
import sys
import db_funcs

# id_counter = 0
    

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
