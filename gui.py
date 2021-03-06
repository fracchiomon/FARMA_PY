import sqlite3 as sql
from sqlite3 import Error
import sys
import db_funcs
import tkinter as tk
from tkinter import Label, StringVar, IntVar, DoubleVar, END

# id_counter = 0

# Root App Configuration

root = tk.Tk()
root.title("FARMA_PY")
root.geometry("800x480")
root.resizable(False, False)


# main function

def main():
    global root
    
    
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

        gui(conn)
        root.mainloop()
        
        scelta2 = 1

        # while (scelta2 == 1):
        #     scelta = db_funcs.menu()
        #     if scelta == 1:
        #         db_funcs.insert_by_user(conn)
        #     elif scelta == 2:
        #         elimina = input(
        #             "Inserisci il Nome (attenzione alle maiuscole) dell'oggetto da eliminare:\t")
        #         db_funcs.delete_item_by_name(conn, elimina)
        #     elif scelta == 3:
        #         db_funcs.print_table(conn)
        #     elif scelta == 4:
        #         stampa = input(
        #             "Inserisci il Nome (attenzione alle maiuscole) dell'oggetto da stampare:\t")
        #         db_funcs.print_by_name(conn, stampa)
        #     elif scelta == -1:
        #         db_funcs.flush_db(conn)
        #     elif scelta == 0:
        #         conn.close()
        #         sys.exit(69)
        #     else:
        #         pass

        #     print(
        #         "\nVuoi effettuare altre operazioni?\nDigita 1 per tornare al menu, 0 per uscire.\n")
        #     scelta2 = int(input())
        #     if scelta2 == 1:
        #         continue
        #     elif scelta2 == 0:
        #         break
        #     else:
        #         print("\nINPUT NON VALIDO.")

        conn.close()
    else:
        print("Error! Cannot connect to DB\n\n")

    return 0



def gui(conn):
    global root
    
    
    # boxes
    name_var = StringVar()
    qty_conf_var = IntVar()
    qty_day_var = DoubleVar()
    ssn_var = IntVar()
    
    name = tk.Entry(root, width = 40, textvariable = name_var)
    name.grid(row = 0, column = 1, padx = 20, ipady = 2)
    
    qty_conf = tk.Entry(root, width = 40, textvariable = qty_conf_var)
    qty_conf.grid(row = 1, column = 1, ipady = 2)
    
    qty_day = tk.Entry(root, width = 40, textvariable = qty_day_var)
    qty_day.grid(row = 2, column = 1, ipady = 2)
    
    ssn = tk.Entry(root, width = 40, textvariable = ssn_var)
    ssn.grid(row = 3, column = 1, ipady = 2)

    # labels
    name_label = Label(root, text = "Nome")
    name_label.grid(row = 0, column = 0)
    qty_conf_label = Label(root, text = "Quantità per Confezione")
    qty_conf_label.grid(row = 1, column = 0)
    qty_day_label = Label(root, text = "Quantità al Giorno\n[ES: 2.5]")
    qty_day_label.grid(row = 2, column = 0)
    ssn_label = Label(root, text = "Coperto da SSN?\n[1: Si || 0: No]")
    ssn_label.grid(row = 3, column = 0)
    
    # submit func
    
    def submit():
        db = r"./DB/farmaci.db"
        conn = sql.connect(db)
        name.delete(0, END)
        qty_conf.delete(0, END)
        qty_day.delete(0, END)
        ssn.delete(0, END)
        # db_funcs.insert_item(conn, name_var, qty_conf_var, qty_day_var, ssn_var)
        # problemi di comunicazione con la funzione
        
        c = conn.cursor()
        c.execute("""INSERT INTO farmaci VALUES (?,?,?,?,?);""", (name_var, qty_conf_var, qty_day_var, ssn_var))
        
        conn.commit()
        conn.close()
        
        
    
    # submit button
    
    submit_btn = tk.Button(root, text = "Inserisci in DB", command = submit())
    submit_btn.grid(row = 4, column = 0, columnspan = 2, ipady = 10, padx = 10, ipadx = 100)

  
    
if __name__ == '__main__':
    main()