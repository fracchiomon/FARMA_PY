import sqlite3 as sql

from sqlite3 import Error

import sys
import db_funcs
import tkinter as tk
from tkinter import Label, StringVar, IntVar, DoubleVar, END, ttk

# id_counter = 0

# Root App Configuration

root = tk.Tk()
root.title("FARMA_PY")
root.geometry("420x250")
root.resizable(False, False)
db = r"./DB/farmaci.db"

# main function

def main():

    db = r"./DB/farmaci.db"
    conn = db_funcs.connect(db)

    sql_create_farmaci_table = """ CREATE TABLE IF NOT EXISTS farmaci (
                                        id integer AUTO_INCREMENT PRIMARY KEY,
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


        conn.close()
    else:
        print("Error! Cannot connect to DB\n\n")

    return 0



def gui(conn):

    # boxes
    name_var = StringVar()
    qty_conf_var = IntVar()
    qty_day_var = DoubleVar()
    ssn_var = IntVar()
    
    
    
    # submit func
    def clear():
        name.delete(0, END)
        qty_conf.delete(0, END)
        qty_day.delete(0, END)
        ssn.delete(0, END)
    
    def submit():
        
        conn = sql.connect(db)
        
        name_var = name.get()
        qty_conf_var = qty_conf.get()
        qty_day_var = qty_day.get()
        ssn_var = ssn.get()
        est = 0.0
        
        int_qty_conf = int(qty_conf_var)
        real_qty_day = float(qty_day_var)
        int_ssn = int(ssn_var)
        if int_ssn != 0:
            int_ssn = 1
        
        if qty_day_var != 0:
            est = int_qty_conf // real_qty_day
        else:
            est = 0.0
        
        
        # db_funcs.insert_item(conn, name_var, qty_conf_var, qty_day_var, ssn_var)
        # problemi di comunicazione con la funzione
        
        c = conn.cursor()
        c.execute("""INSERT INTO farmaci VALUES (?,?,?,?,?);""", (name_var, qty_conf_var, qty_day_var, est, ssn_var))
        
        conn.commit()
        conn.close()
        
        print("INSERIMENTO AVVENUTO\n")
        return
        
      
    # def print_table():
    #     db = r"./DB/farmaci.db"
    #     conn = sql.connect(db)
    #     c = conn.cursor()
        
        
    #     conn.commit()
    #     conn.close()
    
    # submit button
    def submit_window():
        sub_win = tk.Tk()
        sub_win.title("FARMA_PY: NEW ITEM")
        sub_win.geometry("420x150")
        sub_win.resizable(False,False)
        
        
        
        name = tk.Entry(sub_win, width = 40)
        name.grid(row = 0, column = 1, padx = 20, ipady = 2)
        
        qty_conf = tk.Entry(sub_win, width = 40)
        qty_conf.grid(row = 1, column = 1, ipady = 2)
        
        qty_day = tk.Entry(sub_win, width = 40)
        qty_day.grid(row = 2, column = 1, ipady = 2)
        
        ssn = tk.Entry(sub_win, width = 40)
        ssn.grid(row = 3, column = 1, ipady = 2)
        


        # labels
        name_label = Label(sub_win, text = "Nome")
        name_label.grid(row = 0, column = 0, sticky=tk.W, padx=5)
        qty_conf_label = Label(sub_win, text = "Quantità per Confezione")
        qty_conf_label.grid(row = 1, column = 0, sticky=tk.W, padx=5)
        qty_day_label = Label(sub_win, text = "Quantità al Giorno\n[ES: 2.5]")
        qty_day_label.grid(row = 2, column = 0, sticky=tk.W, padx=5)
        ssn_label = Label(sub_win, text = "Coperto da SSN?\n[1: Si || 0: No]")
        ssn_label.grid(row = 3, column = 0, sticky=tk.W, padx=5)
        
        close_btn = ttk.Button (sub_win, text="Chiudi Finestra", command=sub_win.destroy)
        close_btn.grid(row=4, column=0)
        
        submit_btn = tk.Button(sub_win, text = "Inserisci in DB", command = submit)
        submit_btn.grid(row = 4, column = 1)
 
    # button to submit window
    
    to_submit_btn = ttk.Button(root, text="Inserisci Nuovo Elemento", command=submit_window)
    to_submit_btn.grid(row=0, column=0, padx=5, pady=10, ipadx=100, ipady=30)    
        
    def view():
    # PRINT BOX
        global db
        
        print_view = tk.Tk()
        print_view.title("FARMA_PY: VIEW DB")
        print_view.geometry("800x260")
        
        rows_list = db_funcs.print_table(db_file=db)
        
        tree = ttk.Treeview(print_view, column=("c1", "c2", "c3", "c4", "c5"), show='headings')
        tree.column("#1", anchor=tk.CENTER)
        tree.heading("#1", text="NAME")
        tree.column("#2", anchor=tk.CENTER)
        tree.heading("#2", text="QTY PER CONF")
        tree.column("#3", anchor=tk.CENTER)
        tree.heading("#3", text="QTY PER DAY")
        tree.column("#4", anchor=tk.CENTER)
        tree.heading("#4", text="ESTIMATED TIME")
        tree.column("#5", anchor=tk.CENTER)
        tree.heading("#5", text="SSN COVERAGE")
        
        tree.grid(row=0, column = 0)        
        
        for row in rows_list:
            print(row)
            tree.insert("", tk.END, values=row)
        
        close_btn = ttk.Button (print_view, text="Chiudi Finestra", command=print_view.destroy)
        close_btn.grid(row=2, column=0, sticky=tk.W)
        
        
        
    def delete_window():
      del_win = tk.Tk()
      del_win.title("FARMA_PY: DELETE")
      del_win.geometry("420x150")
      del_win.resizable(False,False)
      
      name = tk.Entry(del_win, width = 40)
      name.grid(row = 0, column = 1, padx = 20, ipady = 2)
      
      name_label = Label(del_win, text = "Nome")
      name_label.grid(row = 0, column = 0, sticky=tk.W, padx=5)
      
      
      def delete_func():
        name_var = name.get()
        name.delete(0, END)
        db_funcs.delete_item_by_name(db, name_var)
        return
      
      
      to_delete_btn = ttk.Button(root, text="Elimina un Elemento", command=delete_window)
      to_delete_btn.grid(row=0,column=1,columnspan=2,padx=5,pady=10,ipadx=100,ipady=30)
      delete_btn = ttk.Button(del_win, text="Cancella Elemento", command=delete_func)
      
      delete_btn.grid(row=1,column=0,sticky=tk.W,padx=5,ipadx=100,ipady=30)
            
      close_btn = ttk.Button (del_win, text="ESCI", command=del_win.destroy)
      close_btn.grid(row=1, column=1, sticky=delete_btn, padx=15, ipady=20)
 
 
 
    close_btn = ttk.Button (root, text="ESCI", command=root.destroy)
    close_btn.grid(row=4, column=1, sticky=tk.E, padx=15, ipady=20)

    
    print_btn = tk.Button(root, text = "STAMPA DB", command = view)
    print_btn.grid(row = 5, column = 0, columnspan = 2, ipady = 10, padx = 10, ipadx = 104, sticky=tk.W)
    
    # cascade menu(s)
    
    drop = tk.Menu(root)
    root.config(menu=drop)
    
    data_func = tk.Menu(drop)
    drop.add_cascade(label="Operazioni", menu=data_func)
    data_func.add_command(label="Inserisci Nuovo Elemento", command=submit_window)
    data_func.add_separator()
    data_func.add_command(label="Visualizza Database", command=view)
    data_func.add_separator()
    data_func.add_command(label="Esci", command=exit)
    
    
    drop_insert = tk.Menu(sub_win)
    sub_win.config(menu=drop_insert)
        
    data_func_insert = tk.Menu(drop_insert)
    drop_insert.add_cascade(labels="Operazioni", menu=data_func_insert)
    data_func_insert.add_command(label="Elimina Elemento", command=delete_window)
    data_func_insert.add_command(label="Visualizza Database", command=view)
    data_func_insert.add_separator()
    data_func_insert.add_command(label="Esci", command=exit)
    
    drop_del = tk.Menu(del_win)
    del_win.config(menu=drop_del)
        
    data_func_del = tk.Menu(drop_del)
    drop_del.add_cascade(labels="Operazioni", menu=data_func_del)
    data_func_del.add_command(label="Inserisci Nuovo Elemento", command=submit_window)
    data_func_del.add_separator()
    data_func_del.add_command(label="Visualizza Database", command=view)
    data_func_del.add_separator()
    data_func_del.add_command(label="Esci", command=exit)
    
    drop_view = tk.Menu(print_view)
    print_view.config(menu=drop_view)
        
    data_func_view = tk.Menu(drop_view)
    drop_view.add_cascade(labels="Operazioni", menu=data_func_view)
    data_func_view.add_command(label="Inserisci Nuovo Elemento", command=submit_window)
    data_func_view.add_separator()
    data_func_view.add_command(label="Elimina Elemento", command=delete_window)
    data_func_view.add_separator()
    data_func_view.add_command(label="Esci", command=exit)
    

# main execution
if __name__ == '__main__':
    main()