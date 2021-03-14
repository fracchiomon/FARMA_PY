import sqlite3 as sql
from sqlite3 import Error
import sys
import os
import db_funcs_terminal

# id_counter = 0
    
def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def main():
    clear()
    db = r"./DB/farmaci.db"
    conn = db_funcs_terminal.connect(db)
    

    sql_create_farmaci_table = """ CREATE TABLE IF NOT EXISTS farmaci (
                                         
                                        name text NOT NULL,
                                        qty_per_conf integer,  
                                        qty_per_day real NOT NULL, 
                                        estimated_time integer, 
                                        ssn integer
                                        );"""


    
    if conn is not None:

        db_funcs_terminal.create_table(conn, sql_create_farmaci_table)

        scelta2 = 1
        
        while (scelta2 == 1):
            scelta = db_funcs_terminal.menu()
            if scelta == 1:
                clear()
                db_funcs_terminal.insert_by_user(conn)
            elif scelta == 2:
                clear()
                elimina = input("Inserisci il Nome (attenzione alle maiuscole) dell'oggetto da eliminare:\t")
                db_funcs_terminal.delete_item_by_name(conn, elimina)
            elif scelta == 3:
                clear()
                db_funcs_terminal.print_table(conn)
            elif scelta == 4:
                clear()
                stampa = input("Inserisci il Nome (attenzione alle maiuscole) dell'oggetto da stampare:\t")
                db_funcs_terminal.print_by_name(conn, stampa)
            elif scelta == -1:
                clear()
                db_funcs_terminal.flush_db(conn)
            elif scelta == 0:
                conn.close()
                sys.exit(69)
            else:
                pass
            
            print("\nVuoi effettuare altre operazioni?\nDigita 1 per tornare al menu, 0 per uscire.\n")
            scelta2 = int(input())
            if scelta2 == 1:
                clear()
                continue
            elif scelta2 == 0:
                clear()
                break
            else:
                print("\nINPUT NON VALIDO.")
                print (sql.Error) 
            
        conn.close()
    else:
        clear()
        print("Error! Cannot connect to DB\n\n")
    
    return 0
    

if __name__ == '__main__':
    main()
