import tkinter

import pymysql


class DatabaseOperation(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def add(self, pizza_id, pizza_name, pizza_toppings, pizza_prize, pizza_vegan):
        db = pymysql.connect(host="localhost", user=self.username, password=self.password, db="sys")
        cursor = db.cursor()
        sql = "insert into PizzaMenu(pizzaid,pizzaname,toppings,prize,vegan) values('%s','%s','%s','%s','%s')" % (
            pizza_id, pizza_name, pizza_toppings, pizza_prize, pizza_vegan)
        try:
            cursor.execute(sql)
            db.commit()
        except Exception as err:
            db.rollback()
            print("Error: ", err)
        db.close()

    def delete(self, pizza_id):
        db = pymysql.connect(host="localhost", user=self.username, password=self.password, db="sys")
        cursor = db.cursor()
        sql = "delete from PizzaMenu where id= %s" % (pizza_id)
        try:
            cursor.execute(sql)
            db.commit()
        except Exception as err:
            db.rollback()
            print("Error", err)
        db.close()

    def Update(self, pizza_id, pizza_prize):
        db = pymysql.connect(host="localhost", user=self.username, password=self.password, db="sys")
        cursor = db.cursor()
        sql = "update PizzaMenu set prize= '%s' where id= '%s'" % (pizza_prize, pizza_id)
        try:
            cursor.execute(sql)
            db.commit()
        except Exception as err:
            db.rollback()
            print("Error: ", err)
        db.close()

    def select(self, pizza_id):
        db = pymysql.connect(host="localhost", user=self.username, password=self.password, db="sys")
        cursor = db.cursor()
        sql = "select pizza_id,pizza_name,price from PizzaMenu where pizza_id like'%s'" % ('%' + pizza_id + '%')
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                pizza_id = row[0]
                pizza_name = row[1]
                price = row[2]
                tkinter.messagebox.showinfo("find it",
                                            "pizza_id=%d,pizza_name=%s,price=%d" % (pizza_id, pizza_name, price))
        except:
            return

    def show(self):
        db = pymysql.connect(host="localhost", user=self.username, password=self.password, db="sys")
        cursor = db.cursor()
        sql = "select * from PizzaMenu"
        try:
            cursor.execute(sql)
            PizzaMenu = cursor.fetchall()
            for row in PizzaMenu:
                print("pizzaid: %s  pizzaname: %s  toppings: %s  prize: %s  vegan：%s" % (
                    row[0], row[1], row[2], row[3], row[4]))
        except:
            db.rollback()


