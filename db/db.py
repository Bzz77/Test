import pymysql

def create_table():
    db = pymysql.connect(host="localhost", user="root", password="", db="sys")
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

def main():
    create_table()
    create()

def create():
    db = pymysql.connect(host="localhost", user="root", password="", db="sys")
    cursor = db.cursor()
    t = [('1', 'Salami', 'Cheese, Salami, Tomato Sauce', 'no','11','15.4','16.79'), ('2', 'Hawwii','Cheese, Pineapple, Tomato Sauce', 'yes','10','14.0','15.26')
         , ('3', 'Salmon', 'Cheese, Salmon, Tomato Sauce', 'no','12','16.8','18.31'), ('4', 'Vegetaria', 'Cheese, Vegetable, Tomato Sauce', 'yes','11','15.4','16.79')
         , ('5', 'Margherita', 'Cheese, Tomato Sauce', 'yes','7','9.8','10.68'), ('6', 'BBQ Meat Lovers', 'Ham, Chorizo, Peperoni, Mozzarella, Cheese, BBQ Sauce', 'no','11','15.4','16.79')
         , ('7', 'BBQ Chicken', 'Bell pepper, Onion, Grilled Chicken, BBQ Sauce', 'no','11','15.4','16.79'), ('8', 'Tuna', 'Cheese, Tuna, Tomato Sauce', 'no','11','15.4','16.79'),
         ('9', 'Pepperoni', 'Cheese, Pepperoni, Tomato Sauce', 'no','7','9.8','10.68'), ('10', 'Bacon', 'Cheese, Bacon,Tomato Sauce', 'no','7','9.8','10.68')
         ,('11', 'Tiramisu','','','3','4.2','4.578'), ('12', 'Matcha cake','','','3','4.2','4.578'), ('13','Apple Juice',' ',' ','2','2.8','3.052'),
         ('14','Coca Cola',' ',' ','2','2.8','3.052'), ('15','Coffee',' ',' ','2','2.8','3.052'), ('16','Water',' ',' ','1','1.4','1.526')]

    try:
        for i in range(0, len(t)):
            sql = "insert into PizzaMenu(id,name,toppings,vegan,prize,prizeaftermargin,prizeafterVAT) values('%s','%s','%s','%s','%s','%s','%s')" % t[i]
            cursor.execute(sql)
        db.commit()
        print("Add successful")
    except Exception as e:
        print("Add menu failed：case%s" % e)
    finally:
        cursor.close()
        db.close()

if __name__ == "__main__":
    main()