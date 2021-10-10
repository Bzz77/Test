import pymysql
import tkinter as tk
import tkinter.messagebox
import sql_operation as s
import sql as s1


class PizzaUI:

    def __init__(self, username, password):
        self.operation = s1.DatabaseOperation(username, password)

    def mainpage(self):
        global window
        window = tk.Tk()
        window.title("Pizza")
        window.geometry('400x400')
        page = tk.Frame(window)
        page.pack()
        tk.Label(window, text="Welcome!", font=("黑体", 20)).pack(pady=10)
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
        # window.destroy()
        self.operation.show()

    def pagechange_main(self):
        window2.destroy()
        self.mainpage()

    def menu_add(self):
        global window2
        window2 = tk.Tk()
        window2.title("Pizza")
        window2.geometry('400x500')

        tk.Label(window2, text="add new pizza", font=("黑体", 20)).grid(row=0, column=1, pady=10)
        tk.Label(window2, text="id：").grid(row=1, column=0, padx=20, pady=20)
        tk.Label(window2, text="name：").grid(row=2, column=0, padx=20, pady=20)
        tk.Label(window2, text="toppings：").grid(row=3, column=0, padx=20, pady=20)
        tk.Label(window2, text="vegan：").grid(row=4, column=0, padx=20, pady=20)
        tk.Label(window2, text="prize：").grid(row=5, column=0, padx=20, pady=20)

        v1 = tk.StringVar()
        v2 = tk.StringVar()
        v3 = tk.StringVar()
        v4 = tk.StringVar()
        v5 = tk.StringVar()

        entry1 = tk.Entry(window2, show=None, textvariable=v1).grid(row=1, column=1)
        entry2 = tk.Entry(window2, show=None, textvariable=v2).grid(row=2, column=1)
        entry3 = tk.Entry(window2, show=None, textvariable=v3).grid(row=3, column=1)
        entry4 = tk.Entry(window2, show=None, textvariable=v4).grid(row=4, column=1)
        entry5 = tk.Entry(window2, show=None, textvariable=v5).grid(row=5, column=1)

        button = tk.Button(window2, text="add",
                           command=self.operation.add(v1.get(), v2.get(), v3.get(), v4.get(), v5.get())).grid(row=6, column=1)
        button2 = tk.Button(window2, text="back", command=self.pagechange_main).grid(row=6, column=2, padx=50)

        window2.mainloop()

    def menu_delete(self):
        global window2
        window2 = tk.Tk()
        window2.title("Pizza")
        window2.geometry('400x300')

        tk.Label(window2, text="delete pizza", font=("黑体", 20)).grid(row=0, column=1, pady=20)
        tk.Label(window2, text="Please enter the id").grid(row=1, column=0, padx=20)

        v6 = tk.StringVar()

        entry1 = tk.Entry(window2, show=None, textvariable=v6).grid(row=1, column=1, pady=40)
        button = tk.Button(window2, text="delete", command=self.operation.delete(v6)).grid(row=2, column=0)
        button2 = tk.Button(window2, text="back", command=self.pagechange_main).grid(row=2, column=1, padx=50)
        window2.mainloop()

    def menu_update(self):
        global window2
        window2 = tk.Tk()
        window2.title("pizza")
        window2.geometry('400x300')

        tk.Label(window2, text="update pizza", font=("黑体", 20)).grid(row=0, column=1, pady=20)
        tk.Label(window2, text="Please enter the id").grid(row=1, column=0, padx=20, pady=20)
        tk.Label(window2, text="Please enter the prize").grid(row=2, column=0, padx=20, pady=20)

        v7 = tk.StringVar()
        v8 = tk.StringVar()

        entry1 = tk.Entry(window2, show=None, textvariable=v7).grid(row=1, column=1)
        entry2 = tk.Entry(window2, show=None, textvariable=v8).grid(row=2, column=1)
        button = tk.Button(window2, text="update", command=self.operation.Update(v7.get(), v8.get())).grid(row=3, column=0)
        button2 = tk.Button(window2, text="back", command=self.pagechange_main).grid(row=3, column=1, padx=50)
        window2.mainloop()

    def menu_select(self):
        global window2
        window2 = tk.Tk()
        window2.title("pizza")
        window2.geometry('400x300')

        tk.Label(window2, text="find pizza", font=("黑体", 20)).grid(row=0, column=1, pady=20)
        tk.Label(window2, text="Please enter the id").grid(row=1, column=0, padx=20)

        v9 = tk.StringVar()

        entry1 = tk.Entry(window2, show=None, textvariable=v9).grid(row=1, column=1, pady=40)
        button = tk.Button(window2, text="find", command=self.operation.select(v9.get())).grid(row=2, column=1)
        button2 = tk.Button(window2, text="back", command=self.pagechange_main).grid(row=2, column=2, padx=50)
        window2.mainloop()
