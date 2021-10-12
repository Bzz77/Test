import pymysql


class db(object):
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def create_table(self):
        db = pymysql.connect(host="localhost", user=self.user, password=self.password, db="sys")
        cursor = db.cursor()
        cursor.execute("DROP TABLE IF EXISTS PizzaMenu")

        sql = """
            create table if not exists PizzaMenu(
            id int not null PRIMARY KEY,
            name VARCHAR(255),
            toppings VARCHAR(255),
            vegan VARCHAR(255),
            prize int,
            prizeaftermargin int,
            prizeafterVAT int
            )
        """
        try:
            cursor.execute(sql)
            print("Build successful")
        except Exception as e:
            print("Build database failed：case%s" % e)
        finally:
            cursor.close()
            db.close()

    def create_tableOrder(self):
        db = pymysql.connect(host="localhost", user=self.user, password=self.password, db="sys")
        cursor = db.cursor()
        cursor.execute("DROP TABLE IF EXISTS OrderMenu")

        sql = """
            create table if not exists OrderMenu(
            id INT not null PRIMARY KEY,
            item VARCHAR(255),
            orderTime VARCHAR(255), 
            deliveryPersonid INT,
            foreign key(deliveryPersonid) references DeliveryPerson(id)
            )
        """
        try:
            cursor.execute(sql)
            print("Build successful")
        except Exception as e:
            print("Build database failed：case%s" % e)
        finally:
            cursor.close()
            db.close()

    def create_tableCustomer(self):
        db = pymysql.connect(host="localhost", user=self.user, password=self.password, db="sys")
        cursor = db.cursor()
        cursor.execute("DROP TABLE IF EXISTS PizzaCustomer")

        sql = """
            create table if not exists PizzaCustomer(
            name VARCHAR(255) not null PRIMARY KEY,
            phonenumber VARCHAR(255),
            address VARCHAR(255),
            numoforders int
            )
        """
        try:
            cursor.execute(sql)
            print("Build successful")
        except Exception as e:
            print("Build database failed：case%s" % e)
        finally:
            cursor.close()
            db.close()

    def create_deliveryPersonDb(self):
        db = pymysql.connect(host="localhost", user=self.user, password=self.password, db="sys")
        cursor = db.cursor()
        cursor.execute("DROP TABLE IF EXISTS DeliveryPerson")

        sql = """
                create table if not exists DeliveryPerson(
                id INT not null PRIMARY KEY,
                areacode VARCHAR(255),
                status VARCHAR(255)
                )
            """
        try:
            cursor.execute(sql)
            print("Build successful")
        except Exception as e:
            print("Build database failed：case%s" % e)
        finally:
            cursor.close()
            db.close()

    def create_deliveryPerson(self):
        db = pymysql.connect(host="localhost", user=self.user, password=self.password, db="sys")
        cursor = db.cursor()
        t = [(1, 'Area 1', 'No work'), (2, 'Area 2', 'No work'), (3, 'Area 1', 'No work'), (4, 'Area 1', 'No work')]
        try:
            for i in range(0, len(t)):
                sql = "insert into DeliveryPerson(id,areacode,status) values('%s','%s','%s')" % \
                      t[i]
                cursor.execute(sql)
            db.commit()
            print("Add successful")
        except Exception as e:
            print("Add menu failed：case%s" % e)
        finally:
            cursor.close()
            db.close()

    def create(self):
        db = pymysql.connect(host="localhost", user=self.user, password=self.password, db="sys")
        cursor = db.cursor()
        t = [('1', 'Salami', 'Cheese, Salami, Tomato Sauce', 'no', '11', '15.4', '16.79'),
             ('2', 'Hawwii', 'Cheese, Pineapple, Tomato Sauce', 'yes', '10', '14.0', '15.26')
            , ('3', 'Salmon', 'Cheese, Salmon, Tomato Sauce', 'no', '12', '16.8', '18.31'),
             ('4', 'Vegetaria', 'Cheese, Vegetable, Tomato Sauce', 'yes', '11', '15.4', '16.79')
            , ('5', 'Margherita', 'Cheese, Tomato Sauce', 'yes', '7', '9.8', '10.68'),
             ('6', 'BBQ Meat Lovers', 'Ham, Chorizo, Peperoni, Mozzarella, Cheese, BBQ Sauce', 'no', '11', '15.4',
              '16.79')
            , ('7', 'BBQ Chicken', 'Bell pepper, Onion, Grilled Chicken, BBQ Sauce', 'no', '11', '15.4', '16.79'),
             ('8', 'Tuna', 'Cheese, Tuna, Tomato Sauce', 'no', '11', '15.4', '16.79'),
             ('9', 'Pepperoni', 'Cheese, Pepperoni, Tomato Sauce', 'no', '7', '9.8', '10.68'),
             ('10', 'Bacon', 'Cheese, Bacon,Tomato Sauce', 'no', '7', '9.8', '10.68')
            , ('11', 'Tiramisu', '', '', '3', '4.2', '4.578'), ('12', 'Matcha cake', '', '', '3', '4.2', '4.578'),
             ('13', 'Apple Juice', ' ', ' ', '2', '2.8', '3.052'),
             ('14', 'Coca Cola', ' ', ' ', '2', '2.8', '3.052'), ('15', 'Coffee', ' ', ' ', '2', '2.8', '3.052'),
             ('16', 'Water', ' ', ' ', '1', '1.4', '1.526')]

        try:
            for i in range(0, len(t)):
                sql = "insert into PizzaMenu(id,name,toppings,vegan,prize,prizeaftermargin,prizeafterVAT) values('%s','%s','%s','%s','%s','%s','%s')" % \
                      t[i]
                cursor.execute(sql)
            db.commit()
            print("Add successful")
        except Exception as e:
            print("Add menu failed：case%s" % e)
        finally:
            cursor.close()
            db.close()

    def main(self):
        self.create_table()
        self.create()
        self.create_tableCustomer()
        self.create_deliveryPersonDb()
        self.create_deliveryPerson()
        self.create_tableOrder()


if __name__ == "__main__":
    db1 = db('root', 'Yo17233510.')
    db1.main()
