import pymysql
import tkinter as tk
import tkinter.messagebox as msg
from tkinter import ttk


class PizzaUI:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def mainpage(self):
        global window
        window = tk.Tk()
        window.title("Pizza")
        window.geometry('400x400')
        page = tk.Frame(window)
        page.pack()
        tk.Label(window, text="Welcome!", font=("Arial", 20)).pack(pady=10)
        button1 = tk.Button(window, text="add", command=self.pagechange_add).pack(pady=10)
        button2 = tk.Button(window, text="delete", command=self.pagechange_delete).pack(pady=10)
        button3 = tk.Button(window, text="update", command=self.pagechange_update).pack(pady=10)
        button4 = tk.Button(window, text="select", command=self.pagechange_select).pack(pady=10)
        button5 = tk.Button(window, text="show", command=self.pagechange_show).pack(pady=10)
        # button5 = tk.Button(window, text="order", command=).pack(pady=10)
        window.mainloop()

    def pagechange_add(self):
        window.destroy()
        self.menu_add()

    def pagechange_delete(self):
        window.destroy()
        self.menu_delete()

    def pagechange_update(self):
        window.destroy()
        self.menu_update()

    def pagechange_select(self):
        window.destroy()
        self.menu_select()

    def pagechange_show(self):
        window.destroy()
        self.menu_show()

    def pagechange_main(self):
        window2.destroy()
        self.mainpage()

    def menu_add(self):
        global window2
        window2 = tk.Tk()
        window2.title("Pizza")
        window2.geometry('400x500')

        tk.Label(window2, text="add new pizza", font=("Arial", 20)).grid(row=0, column=1, pady=10)
        tk.Label(window2, text="id：").grid(row=1, column=0, padx=20, pady=20)
        tk.Label(window2, text="name：").grid(row=2, column=0, padx=20, pady=20)
        tk.Label(window2, text="toppings：").grid(row=3, column=0, padx=20, pady=20)
        tk.Label(window2, text="vegan：").grid(row=4, column=0, padx=20, pady=20)
        tk.Label(window2, text="prize：").grid(row=5, column=0, padx=20, pady=20)

        global entry1
        entry1 = tk.Entry(window2, show=None)
        entry1.grid(row=1, column=1)
        global entry2
        entry2 = tk.Entry(window2, show=None)
        entry2.grid(row=2, column=1)
        global entry3
        entry3 = tk.Entry(window2, show=None)
        entry3.grid(row=3, column=1)
        global entry4
        entry4 = tk.Entry(window2, show=None)
        entry4.grid(row=4, column=1)
        global entry5
        entry5 = tk.Entry(window2, show=None)
        entry5.grid(row=5, column=1)

        button = tk.Button(window2, text="add", command=self.add).grid(row=6, column=1)
        button2 = tk.Button(window2, text="back", command=self.pagechange_main).grid(row=6, column=2, padx=50)

        window2.mainloop()

    def menu_delete(self):
        global window2
        window2 = tk.Tk()
        window2.title("Pizza")
        window2.geometry('400x300')

        tk.Label(window2, text="delete pizza", font=("Arial", 20)).grid(row=0, column=1, pady=20)
        tk.Label(window2, text="Please enter the id").grid(row=1, column=0, padx=20)

        global entry6
        entry6 = tk.Entry(window2, show=None)
        entry6.grid(row=1, column=1, pady=40)
        button = tk.Button(window2, text="delete", command=self.delete).grid(row=2, column=0)
        button2 = tk.Button(window2, text="back", command=self.pagechange_main).grid(row=2, column=1, padx=50)
        window2.mainloop()

    def menu_update(self):
        global window2
        window2 = tk.Tk()
        window2.title("pizza")
        window2.geometry('400x300')

        tk.Label(window2, text="update pizza", font=("Arial", 20)).grid(row=0, column=1, pady=20)
        tk.Label(window2, text="Please enter the id").grid(row=1, column=0, padx=20, pady=20)
        tk.Label(window2, text="Please enter the prize").grid(row=2, column=0, padx=20, pady=20)

        global entry7
        global entry8
        entry7 = tk.Entry(window2, show=None)
        entry7.grid(row=1, column=1)
        entry8 = tk.Entry(window2, show=None)
        entry8.grid(row=2, column=1)
        button = tk.Button(window2, text="update", command=self.Update).grid(row=3, column=0)
        button2 = tk.Button(window2, text="back", command=self.pagechange_main).grid(row=3, column=1, padx=50)
        window2.mainloop()

    def menu_select(self):
        global window2
        window2 = tk.Tk()
        window2.title("pizza")
        window2.geometry('400x300')

        tk.Label(window2, text="find pizza", font=("Arial", 20)).grid(row=0, column=1, pady=20)
        tk.Label(window2, text="Please enter the id").grid(row=1, column=0, padx=20)

        global entry9
        entry9 = tk.Entry(window2, show=None)
        entry9.grid(row=1, column=1, pady=40)
        button = tk.Button(window2, text="find", command=self.select).grid(row=2, column=1)
        button2 = tk.Button(window2, text="back", command=self.pagechange_main).grid(row=2, column=2, padx=50)
        window2.mainloop()

    def menu_show(self):
        global window2
        window2 = tk.Tk()
        window2.title('Pizza Menu')
        window2.geometry('1500x500')

        tk.Button(window2, text='show', font=('Arial', 12), width=10, command=self.show).place(x=900, y=25)
        button2 = tk.Button(window2, text="back", command=self.pagechange_main).place(x=900, y = 425)

        global tree
        yscrollbar = ttk.Scrollbar(window2, orient='vertical')
        tree = ttk.Treeview(window2, columns=('1', '2', '3', '4', '5', '6', '7'), show="headings",yscrollcommand=yscrollbar.set)
        tree.column('1', width=50, anchor='center')
        tree.column('2', width=150, anchor='center')
        tree.column('3', width=350, anchor='center')
        tree.column('4', width=50, anchor='center')
        tree.column('5', width=50, anchor='center')
        tree.column('6', width=150, anchor='center')
        tree.column('7', width=150, anchor='center')

        tree.heading('1', text='ID')
        tree.heading('2', text='Name')
        tree.heading('3', text='Pizza toppings')
        tree.heading('4', text='Vegan')
        tree.heading('5', text='prize')
        tree.heading('6', text='prize after margin')
        tree.heading('7', text='prize after VAT')
        tree.place(x=200, y=150)
        yscrollbar.place(x=1150, y=150)
        window.mainloop()

    def add(self):
        db = pymysql.connect(host="localhost", user=self.username, password=self.password, db="sys")
        cursor = db.cursor()
        sql = "insert into PizzaMenu(id,name,toppings,vegan,prize,prizeaftermargin,prizeafterVAT) values('%s','%s','%s','%s','%s','%s','%s')" % (
            entry1.get(), entry2.get(), entry3.get(), entry4.get(), entry5.get(), round(float(entry5.get())) * 1.4,
            round(float(entry5.get())) * 1.4 * 1.09)

        try:
            cursor.execute(sql)
            db.commit()
        except Exception as err:
            db.rollback()
            print("Error: ", err)
        msg.showinfo(title='success!', message='add new pizza')
        db.close()

    def delete(self):
        db = pymysql.connect(host="localhost", user=self.username, password=self.password, db="sys")
        cursor = db.cursor()
        sql = "delete from PizzaMenu where id= %s" % (entry6.get())
        try:
            cursor.execute(sql)
            db.commit()
        except Exception as err:
            db.rollback()
            print("Error", err)
        msg.showinfo(title='success!', message='delete pizza')
        db.close()

    def Update(self):
        db = pymysql.connect(host="localhost", user=self.username, password=self.password, db="sys")
        cursor = db.cursor()
        sql = "update PizzaMenu set prize= '%s',prizeaftermargin = '%s',prizeafterVAT = '%s' where id= '%s'" % (
        entry8.get(),
        round(float(entry8.get())) * 1.4, round(float(entry8.get())) * 1.4 * 1.09, entry7.get())

        try:
            cursor.execute(sql)
            db.commit()
        except Exception as err:
            db.rollback()
            print("Error: ", err)
        msg.showinfo(title='success!', message='update pizza')
        db.close()

    def select(self):
        db = pymysql.connect(host="localhost", user=self.username, password=self.password, db="sys")
        cursor = db.cursor()
        sql = "select * from PizzaMenu where id like '%s'" % ('%' + entry9.get() + '%')
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                msg.showinfo("find it",
                             "id: %s, name: %s, toppings: %s, vegan：%s, prize: %d, prize after margin: %d, prize after VAT: %d" %
                             (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        except:
            return
        db.close()

    def show(self):
        db = pymysql.connect(host="localhost", user=self.username, password=self.password, db="sys")
        cursor = db.cursor()
        sql = "select * from PizzaMenu"
        try:
            cursor.execute(sql)
            PizzaMenu = cursor.fetchall()
            i = 1
            for row in PizzaMenu:
                # print(
                #     "pizzaid: %s  pizzaname: %s  toppings: %s   vegan：%s   prize: %d   prize after margin: %d   prize after VAT: %d" % (
                #         row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
                tree.insert('', i, values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
                i = i + 1
        except:
            db.rollback()
        db.close()
