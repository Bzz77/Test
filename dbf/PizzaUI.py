import random
import pymysql
import tkinter as tk
import tkinter.messagebox as msg
from tkinter import ttk
import datetime


class PizzaUI:

    # Window for login
    def creatp(self):
        global window3
        window3 = tk.Tk()
        window3.title("Login Window")
        window3.geometry("1000x600+100+50")

        # Login Frame
        Frame_login = tk.Frame(window3, bg="white")
        Frame_login.place(x=250, y=100, width=500, height=400)

        # Title & subtitle
        title = tk.Label(Frame_login, text="Welcome Pizza Shop", font=("Arial", 25, "bold"), fg="#6162FF", bg="white")
        title.place(x=90, y=30)
        subtitle = tk.Label(Frame_login, text="Login Here!", font=("Arial", 15, "bold"), fg="#1d1d1d", bg="white")
        subtitle.place(x=90, y=100)

        global user2
        user1 = tk.Label(Frame_login, text="Username", font=("Arial", 15, "bold"), fg="grey", bg="white")
        user1.place(x=90, y=140)
        user2 = tk.Entry(Frame_login, show=None, font=("Arial", 15), bg="#E7E6E6")
        user2.place(x=90, y=170, width=320, height=35)

        global password2
        password1 = tk.Label(Frame_login, text="Password", font=("Arial", 15, "bold"), fg="grey", bg="white")
        password1.place(x=90, y=210)
        password2 = tk.Entry(Frame_login, show='*', font=("Arial", 15), bg="#E7E6E6")
        password2.place(x=90, y=240, width=320, height=35)

        submit = tk.Button(Frame_login, command=self.check_function, cursor="hand2", text="Log in!", bd=0,font=("Arial", 12), fg="white", bg="blue")
        submit.place(x=90, y=320, width=180, height=40)

        window3.mainloop()

    def check_function(self):
        try:
           db = pymysql.connect(host="localhost", user=user2.get(), password=password2.get(), db="sys")
        except Exception as err:
            print("Error: ", err)
            exit()
        self.username = user2.get()
        self.password = password2.get()
        window3.destroy()
        self.mainpage()

    # Window for MainMenu
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
        button6 = tk.Button(window, text="order", command=self.pagechange_order).pack(pady=10)
        window.mainloop()

    # Function of page change
    def pagechange_add(self):
        window.destroy()
        self.menu_add()

    def pagechange_addC(self):
        window2.destroy()
        self.menu_addCustomer()

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

    def pagechange_order(self):
        window.destroy()
        self.menu_order()

    # window for details of Pizza order
    def menu_order(self):
        global window2
        window2 = tk.Tk()
        window2.title("Oeder System and Menu")
        window2.geometry("1200x600+100+50")
        global e
        e = []
        global m
        m = [16.79, 15.26, 18.31, 16.79, 10.68, 16.79, 16.79, 16.79, 10.68, 10.68, 4.578, 4.578, 3.052, 3.052, 3.052,
             1.526]
        global e1
        lab1 = tk.Label(window2, text="1. Salami: Cheese, Salami, Tomato Sauce (no,11,15.4) - €16.79",
                        font=("Arial", 10, "bold"), fg="grey", bg="white")
        lab1.place(x=0, y=0)
        e1 = tk.Entry(window2, show=None, font=("Arial", 15), bg="#E7E6E6")
        e1.place(x=0, y=25, width=400, height=20)
        e.append(e1)
        global e2
        lab2 = tk.Label(window2, text="2. Hawwii: Cheese, Pineapple, Tomato Sauce (yes,10,14.0) - €15.26",
                        font=("Arial", 10, "bold"), fg="grey", bg="white")
        lab2.place(x=0, y=45)
        e2 = tk.Entry(window2, show=None, font=("Arial", 15), bg="#E7E6E6")
        e2.place(x=0, y=70, width=400, height=20)
        e.append(e2)
        global e3
        lab3 = tk.Label(window2, text="3. Salmon: Cheese, Salmon, Tomato Sauce (no,12,16.8) - €18.31",
                        font=("Arial", 10, "bold"), fg="grey", bg="white")
        lab3.place(x=0, y=90)
        e3 = tk.Entry(window2, show=None, font=("Arial", 15), bg="#E7E6E6")
        e3.place(x=0, y=115, width=400, height=20)
        e.append(e3)
        global e4
        lab4 = tk.Label(window2, text="4. Vegetaria: Cheese, Vegetable, Tomato Sauce (yes,11,15.4) - €16.79",
                        font=("Arial", 10, "bold"), fg="grey", bg="white")
        lab4.place(x=0, y=135)
        e4 = tk.Entry(window2, show=None, font=("Arial", 15), bg="#E7E6E6")
        e4.place(x=0, y=160, width=400, height=20)
        e.append(e4)
        global e5
        lab5 = tk.Label(window2, text="5. eMargherita: Cheese, Tomato Sauce (yes,7,9.8) - €10.68",
                        font=("Arial", 10, "bold"), fg="grey", bg="white")
        lab5.place(x=0, y=180)
        e5 = tk.Entry(window2, show=None, font=("Arial", 15), bg="#E7E6E6")
        e5.place(x=0, y=205, width=400, height=20)
        e.append(e5)
        global e6
        lab6 = tk.Label(window2,
                        text="6. BBQ Meat Lovers: Ham, Peperoni, MozzarellaCheese, BBQ Sauce (no,11,15.4) - €16.79",
                        font=("Arial", 10, "bold"), fg="grey", bg="white")
        lab6.place(x=0, y=225)
        e6 = tk.Entry(window2, show=None, font=("Arial", 15), bg="#E7E6E6")
        e6.place(x=0, y=250, width=400, height=20)
        e.append(e6)
        global e7
        lab7 = tk.Label(window2,
                        text="7. BBQ Chicken: Bell pepper, Onion, Grilled Chicken, BBQ Sauce (no,11,15.4) - €16.79",
                        font=("Arial", 10, "bold"), fg="grey", bg="white")
        lab7.place(x=0, y=270)
        e7 = tk.Entry(window2, show=None, font=("Arial", 15), bg="#E7E6E6")
        e7.place(x=0, y=305, width=400, height=20)
        e.append(e7)
        global e8
        lab8 = tk.Label(window2, text="8. Tuna: Cheese, Tuna, Tomato Sauce (no,11,15.4) - €16.79",
                        font=("Arial", 10, "bold"), fg="grey", bg="white")
        lab8.place(x=0, y=325)
        e8 = tk.Entry(window2, show=None, font=("Arial", 15), bg="#E7E6E6")
        e8.place(x=0, y=350, width=400, height=20)
        e.append(e8)
        global e9
        lab9 = tk.Label(window2, text="9. Pepperoni: Cheese, Pepperoni, Tomato Sauce (no,7,9.8) - €10.68",
                        font=("Arial", 10, "bold"), fg="grey", bg="white")
        lab9.place(x=0, y=375)
        e9 = tk.Entry(window2, show=None, font=("Arial", 15), bg="#E7E6E6")
        e9.place(x=0, y=400, width=400, height=20)
        e.append(e9)
        global e10
        lab10 = tk.Label(window2, text="10. Bacon: Cheese, Bacon, Tomato Sauce (no,7,9.8) - €10.68",
                         font=("Arial", 10, "bold"), fg="grey", bg="white")
        lab10.place(x=0, y=425)
        e10 = tk.Entry(window2, show=None, font=("Arial", 15), bg="#E7E6E6")
        e10.place(x=0, y=450, width=400, height=20)
        e.append(e10)
        global e11
        lab11 = tk.Label(window2, text="11. Tiramisu (3,4.2) - €4.578", font=("Arial", 10, "bold"), fg="grey",
                         bg="white")
        lab11.place(x=750, y=0)
        e11 = tk.Entry(window2, show=None, font=("Arial", 15), bg="#E7E6E6")
        e11.place(x=750, y=25, width=400, height=20)
        e.append(e11)
        global e12
        lab12 = tk.Label(window2, text="12. Matcha cake (3,4.2) - €4.578", font=("Arial", 10, "bold"), fg="grey",
                         bg="white")
        lab12.place(x=750, y=45)
        e12 = tk.Entry(window2, show=None, font=("Arial", 15), bg="#E7E6E6")
        e12.place(x=750, y=70, width=400, height=20)
        e.append(e12)
        global e13
        lab13 = tk.Label(window2, text="13. Apple Juice (2,2.8) - €3.052", font=("Arial", 10, "bold"), fg="grey",
                         bg="white")
        lab13.place(x=750, y=90)
        e13 = tk.Entry(window2, show=None, font=("Arial", 15), bg="#E7E6E6")
        e13.place(x=750, y=115, width=400, height=20)
        e.append(e13)
        global e14
        lab14 = tk.Label(window2, text="14. Coca Cola (2,2.8) - €3.052", font=("Arial", 10, "bold"), fg="grey",
                         bg="white")
        lab14.place(x=750, y=135)
        e14 = tk.Entry(window2, show=None, font=("Arial", 15), bg="#E7E6E6")
        e14.place(x=750, y=160, width=400, height=20)
        e.append(e14)
        global e15
        lab15 = tk.Label(window2, text="15. Coffee (2,2.8) - €3.052", font=("Arial", 10, "bold"), fg="grey", bg="white")
        lab15.place(x=750, y=180)
        e15 = tk.Entry(window2, show=None, font=("Arial", 15), bg="#E7E6E6")
        e15.place(x=750, y=205, width=400, height=20)
        e.append(e15)
        global e16
        lab16 = tk.Label(window2, text="16. Water (1,1.4) - €1.526", font=("Arial", 10, "bold"), fg="grey", bg="white")
        lab16.place(x=750, y=225)
        e16 = tk.Entry(window2, show=None, font=("Arial", 15), bg="#E7E6E6")
        e16.place(x=750, y=250, width=400, height=20)
        e.append(e16)

        for i in range(0, len(e)):
            e[i].insert(0, '0')

        global e17
        lab17 = tk.Label(window2, text="Discount code", font=("Arial", 10, "bold"), fg="grey", bg="white")
        lab17.place(x=750, y=275)
        e17 = tk.Entry(window2, show=None, font=("Arial", 15), bg="#E7E6E6")
        e17.place(x=750, y=300, width=200, height=20)
        e17.insert(0, 'None')
        pay = tk.Button(window2, command=self.print_total, cursor="hand2", text="Finish", bd=0, font=("Arial", 12),
                        fg="white", bg="blue")
        pay.place(x=800, y=350, width=180, height=40)

        button2 = tk.Button(window2, text="back", command=self.pagechange_main)
        button2.place(x=800, y=400, width=180, height=40)

        button2 = tk.Button(window2, text="customer", command=self.pagechange_addC)
        button2.place(x=800, y=450, width=180, height=40)

        window2.mainloop()

    # window for details of Pizza database
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

    # window for details of Pizza database
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

    # window for details of Pizza database
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

    # window for details of Pizza database
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

    # window for details of Pizza database
    def menu_show(self):
        global window2
        window2 = tk.Tk()
        window2.title('Pizza Menu')
        window2.geometry('1500x500')

        tk.Button(window2, text='show', font=('Arial', 12), width=10, command=self.show).place(x=900, y=25)
        button2 = tk.Button(window2, text="back", command=self.pagechange_main).place(x=900, y=425)

        global tree
        yscrollbar = ttk.Scrollbar(window2, orient='vertical')
        tree = ttk.Treeview(window2, columns=('1', '2', '3', '4', '5', '6', '7'), show="headings",
                            yscrollcommand=yscrollbar.set)
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

    # window for details of customer
    def menu_addCustomer(self):
        global window2
        window2 = tk.Tk()
        window2.title("Pizza")
        window2.geometry('600x500')

        tk.Label(window2, text="Enter your information", font=("Arial", 20)).grid(row=0, column=1, pady=10)
        tk.Label(window2, text="Name：").grid(row=1, column=0, padx=20, pady=20)
        tk.Label(window2, text="Phone numbers：").grid(row=2, column=0, padx=20, pady=20)
        tk.Label(window2, text="Address：").grid(row=3, column=0, padx=20, pady=20)

        global entry10
        entry10 = tk.Entry(window2, show=None)
        entry10.grid(row=1, column=1)
        global entry11
        entry11 = tk.Entry(window2, show=None)
        entry11.grid(row=2, column=1)
        global entry12
        entry12 = tk.Entry(window2, show=None)
        entry12.grid(row=3, column=1)

        button = tk.Button(window2, text="add", command=self.customer_add).grid(row=6, column=0)
        button2 = tk.Button(window2, text="back", command=self.pagechange_main).grid(row=6, column=1, padx=50)

        window2.mainloop()

    # add function for customer and decide the order with delivery person
    def customer_add(self):
        db = pymysql.connect(host="localhost", user=self.username, password=self.password, db="sys")
        cursor = db.cursor()
        num = random.randint(1, 500)
        sql = "insert into PizzaCustomer(name,phonenumber,address,numoforders) values('%s','%s','%s','%s')" % (
            entry10.get(), entry11.get(), entry12.get(), num)
        try:
            cursor.execute(sql)
            db.commit()
        except Exception as err:
            db.rollback()
            print("Error: ", err)
        num1 = str(random.randint(1, 4))
        sql = "insert into OrderMenu(id,orderTime,deliveryPersonid) values('%s','%s','%s')" % (
        num, str(datetime.datetime.now()), num1)
        try:
            cursor.execute(sql)
            db.commit()
        except Exception as err:
            db.rollback()
            print("Error: ", err)
        sql = "update DeliveryPerson set status = '%s' where id = '%s' " % ('Working', num1)
        try:
            cursor.execute(sql)
            db.commit()
        except Exception as err:
            db.rollback()
            print("Error: ", err)
        msg.showinfo(title='success!', message='add new customer, and successfully ordered.')
        print('Your order has been received and is being processed.')
        print('The order will be delivered in 5 mins')
        ask = input("Do you want to cancel the order?  ")
        if ask == "yes" or ask == "Yes" or ask == "YES":
            print("Your order has been cancelled")
            exit()
        print('The estimated delivery time is: ' + str(datetime.datetime.now() + datetime.timedelta(minutes=15)))
        sql = "update DeliveryPerson set status = '%s' where id = '%s' " % ('No work', num1)
        try:
            cursor.execute(sql)
            db.commit()
        except Exception as err:
            db.rollback()
            print("Error: ", err)
        db.close()

    # add the stuff from database
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

    # delete the stuff from database
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

    # update the stuff from database
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

    # Show the specific  stuff from database
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

    # Show the stuff from database
    def show(self):
        db = pymysql.connect(host="localhost", user=self.username, password=self.password, db="sys")
        cursor = db.cursor()
        sql = "select * from PizzaMenu"
        try:
            cursor.execute(sql)
            PizzaMenu = cursor.fetchall()
            i = 1
            for row in PizzaMenu:
                tree.insert('', i, values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
                i = i + 1
        except:
            db.rollback()
        db.close()

    # print the fees of order
    def print_total(self):
        total = 0
        for i in range(0, len(e)):
            if e[i].get() != '0':
                total = total + round(float(e[i].get())) * m[i]

        if e17.get() != 'None':
            total = int(total * 0.9)
        lab17 = tk.Label(window2, text=total, font=("Arial", 10, "bold"), fg="grey", bg="white")
        lab17.place(x=1000, y=375)


# Please run the db.py first for building database in your device
# Create GUI
if __name__ == '__main__':
    p = PizzaUI()
    p.creatp()
