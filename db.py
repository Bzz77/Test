import pymysql

def create_table():
    db = pymysql.connect(host="localhost", user="root", password="", db="sys")
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS PizzaMenu")

    sql = """
        create table PizzaMenu(
        pizzaid int not null AUTO_INCREMENT PRIMARY KEY,
        pizzaname VARCHAR(255),
        toppings VARCHAR(255),
        vegan VARCHAR(255),
        prize int,
        prizemargin int,
        prizeVAT int
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

if __name__ == "__main__":
    main()