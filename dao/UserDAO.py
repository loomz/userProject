from dao import mysqlPool
from model.User import User


def get(id):
    try:
        con = mysqlPool.pool.get_connection()
        cursor = con.cursor()
        cursor.execute("select * from user where id=%s" % id)
        result = cursor.fetchall()

        name = result[0]["name"]
        print("dao get user=%s" % name)
    except Exception as e:
        print(e)
        return None
    finally:
        con.close()


def insert(user: User):
    print("insert user=%s" % user.name)
    try:
        con = mysqlPool.pool.get_connection()
        cursor = con.cursor()
        con.start_transaction()
        cursor.execute("insert into user(name, age, sex, birth) values('%s', %s, '%s') "
                       % (user.name, user.age, user.sex, user.birth))
        con.commit()
    except Exception as e:
        print(e)
        if "con" in dir():
            con.rollback()
    finally:
        if "con" in dir():
            con.close()

def update(user: User):
    try:
        con = mysqlPool.pool.get_connection()
        cursor = con.cursor()
        con.start_transaction()
        cursor.execute("update user set name='%s', birth='%s' " % (user.name, user.birth))
        con.commit()
    except Exception as e:
        print(e)
        if "con" in dir():
            con.rollback()
    finally:
        if "con" in dir():
            con.close()




