import db_funcs_terminal
import sqlite3 as sql
import sys
import os


# id_counter = 0

def clear():
    """Funzione per ripulire la console, controlla se ci si trova su
    ambiente Windows o UNIX/ecc... e manda il rispettivo comando"""

    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def main():
    """Funzione Main, chiamata all'avvio del programma"""

    clear()

    # memorizzo la posizione del DB
    db = r"./DB/farmaci.db"
    
    # connessione al DB
    conn = db_funcs_terminal.connect(db)
    
    # prototipazione della tabella 'farmaci' se non esiste nel DB
    sql_create_farmaci_table = """ CREATE TABLE IF NOT EXISTS farmaci (
                                         
                                        name text NOT NULL,
                                        qty_per_conf integer,  
                                        qty_per_day real NOT NULL, 
                                        estimated_time integer, 
                                        ssn integer
                                        );"""


    # se la connessione ha successo svolgo il programma
    if conn is not None:

        # creazione tabella
        db_funcs_terminal.create_table(conn, sql_create_farmaci_table)

        # "HomePage" - Scelta dell'utente
        scelta2 = 1
        while (scelta2 == 1):
            scelta = db_funcs_terminal.menu()
            if scelta == 1:
                # scelta = 1 -> Inserimento
                clear()
                db_funcs_terminal.insert_by_user(conn)
            elif scelta == 2:
                # scelta = 2 -> Cancellazione
                clear()
                elimina = input("Inserisci il Nome (attenzione alle maiuscole) dell'oggetto da eliminare:\t")
                db_funcs_terminal.delete_item_by_name(conn, elimina)
            elif scelta == 3:
                # scelta = 3 -> Stampa DB
                clear()
                db_funcs_terminal.print_table(conn)
            elif scelta == 4:
                # scelta = 4 -> Stampa singolo oggetto DB tramite il nome
                clear()
                stampa = input("Inserisci il Nome (attenzione alle maiuscole) dell'oggetto da stampare:\t")
                db_funcs_terminal.print_by_name(conn, stampa)
            elif scelta == -1:
                # scelta = -1 -> Cancellazione Tabella (previa conferma)
                clear()
                db_funcs_terminal.flush_db(conn)
            elif scelta == 0:
                # scelta = 0 -> Uscita
                conn.close()
                sys.exit("Program aborted by User")
            else:
                pass
            
            # fine operazione, richiesta di nuovo input
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
        # fine programma, chiamo una chiusura "di sicurezza" della connessione
        conn.close()
    else:
        clear()
        print("Error! Cannot connect to DB\n\n")
    
    return 0
    

# Main program
if __name__ == '__main__':
    main()
