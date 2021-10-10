import tkinter

import pymysql

# round(float())
class DatabaseOperation(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def add(self, pizza_id, pizza_name, pizza_toppings, pizza_vegan, pizza_prize):
        prize_margin = round(float(pizza_prize)) * 1.4
        prize_VAT = prize_margin * 1.09
        db = pymysql.connect(host="localhost", user=self.username, password=self.password, db="sys")
        cursor = db.cursor()
        sql = "insert into PizzaMenu(pizzaid,pizzaname,toppings,vegan,prize,prizemargin,prizeVAT) values('%s','%s','%s','%s','%d','%d','%d')" % (
            pizza_id, pizza_name, pizza_toppings, pizza_vegan, round(float(pizza_prize)), prize_margin, prize_VAT)
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
        sql = "update PizzaMenu set prize= '%d',prizemargin = '%d',prizeVAT = '%d' where id= '%s'" % (round(float(pizza_prize)), round(float(pizza_prize)) * 1.4, round(float(pizza_prize)) * 1.4 * 1.09, pizza_id)
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
                tkinter.messagebox.showinfo("find it",
                                            "pizzaid: %s  pizzaname: %s  toppings: %s   vegan：%s   prize: %d   prize after margin: %d   prize after VAT: %d" %
                                            (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
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
                print("pizzaid: %s  pizzaname: %s  toppings: %s   vegan：%s   prize: %d   prize after margin: %d   prize after VAT: %d" % (
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        except:
            db.rollback()


